a
    ʎ(gd  �                   @   s�   d dl mZ d dlmZmZmZ d dlmZ ddlmZ ddl	m
Z
 d dlZd dlZdd	� Zee�d
dd��ZG dd� dej�ZG dd� dej�ZdS )�    )�Image)�api�fields�models)�ValidationError�   )�Messager)�ConfigNc                 C   s,   t �� }| �|d� |�d� t�|�� �S )NZJPEGr   )�io�BytesIOZsave�seek�base64Z	b64encode�read)�image�f� r   �models/connection.py�encode_image_to_base64
   s    
r   ZRGB)�   r   )��   r   r   c                       s6   e Zd ZdZdZejdd�Zej	� fdd��Z
�  ZS )�	LoginMenu�whatsapp.login_menuz
Login MenuzQR Code)�stringc                    s4   t t| ��|�}d| jjv r0| jjd }||d< |S )N�qrcode)�superr   �default_get�env�context)�selfr   �resr   ��	__class__r   r   r      s
    zLoginMenu.default_get)�__name__�
__module__�__qualname__�_name�_descriptionr   r   r   r   Zmodelr   �__classcell__r   r   r    r   r      s
   r   c                
   @   s�   e Zd ZdZdZdgZejddd�Zejddd�Z	ej
dddd	�Zej
d
ddd	�Zejdddd	�Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zd*eeeedd�dd�Zed d!� �Zd+eeeeeeeed%�d&d'�Zd(d)� ZdS ),�
Connectionzwhatsapp.connectionzWhatsapp Connectionzmail.thread�NameT)r   �requiredzAPI KeyZActive)r   �defaultr*   z	Logged InFzRequests Left Todayr   c                 C   s   t | ��d| j� d S )NZdefault_connection)r	   �set�id�r   r   r   r   �set_as_default_connection0   s    z$Connection.set_as_default_connectionc                 C   s`   | D ]V}|� �  |jrtd��|js&qt|j�}|�� }t|�}dddd| j|d�d�  S d S )NzAlready logged in!zir.actions.act_windowZformr   �new)�orderr   )�typeZ	view_modeZ	res_model�targetr   )�check_status�	logged_inr   �client_secretr   Zauthenticater   r-   )r   �record�messagerZpillow_imageZbase64_imager   r   r   �login3   s    

�zConnection.loginc                 C   s   t | j�j}|�dd�| _d S )NZremaining_requestsr   )r   r6   �requests_info�get�requests_left)r   r:   r   r   r   �check_left_requestsJ   s    zConnection.check_left_requestsc              
   C   sP   zt | j��� | _| ��  W n. tyJ } z| �|� W Y d }~n
d }~0 0 d S �N)r   r6   Zis_logged_inr5   r=   �ChildProcessError�handle_exception)r   �er   r   r   r4   N   s
    zConnection.check_statusc                 C   s   t | j���  d S r>   )r   r6   �logoutr.   r   r   r   rB   U   s    zConnection.logoutc              
   C   sV   z"t | j�}|�|� |�|� W n. tyP } z| �|� W Y d }~n
d }~0 0 d S r>   )r   r6   �set_receiver�send_messager?   r@   )r   �to_phone_number�messager8   rA   r   r   r   rD   X   s    

zConnection.send_message�document� N)rE   �data�filename�caption�returnc              
   C   sb   | � �  z&t| j�}|�|� |�|||� W n. ty\ } z| �|� W Y d }~n
d }~0 0 d S r>   )Z
ensure_oner   r6   rC   �send_pdfr?   r@   )r   rE   rI   rJ   rK   r8   rA   r   r   r   rM   `   s    

zConnection.send_pdfc                 C   s   t | t�rtt| ���n� d S r>   )�
isinstancer?   r   �str)rA   r   r   r   r@   j   s    
zConnection.handle_exceptionr   �jpg�sendFile)rE   rI   rJ   �filetyperK   �include_prefix�already_in_base64�	link_pathc	              
   C   sb   z.t | j�}	|	�|� |	�|||||||� W n. ty\ }
 z| �|
� W Y d }
~
n
d }
~
0 0 d S r>   )r   r6   rC   �	send_filer?   r@   )r   rE   rI   rJ   rR   rK   rS   rT   rU   r8   rA   r   r   r   rV   q   s    

zConnection.send_filec              
   C   sD   zt | j��� W S  ty> } z| �|� W Y d }~n
d }~0 0 d S r>   )r   r6   �get_contactsr?   r@   )r   Z	exceptionrA   r   r   r   rW   �   s    zConnection.get_contacts)rG   rH   )r   rP   rH   TFrQ   )r"   r#   r$   r%   r&   Z_inheritr   ZChar�namer6   ZBooleanZactiver5   ZIntegerr<   r/   r9   r=   r4   rB   rD   rO   �bytesrM   �staticmethodr@   �boolrV   rW   r   r   r   r   r(   %   sD   

	      ��r(   )ZPILr   Zodoor   r   r   Zodoo.exceptionsr   r   Z	global_pyr	   r   r
   r   r0   ZBLANK_IMAGEZTransientModelr   ZModelr(   r   r   r   r   �<module>   s   