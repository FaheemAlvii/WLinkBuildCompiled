a
    ʎ(g�	  �                   @   sZ   d dl mZmZmZ d dlmZ ddlmZmZm	Z	m
Z
mZmZmZ G dd� dej�ZdS )�    )�api�fields�models)�ValidationError�   )�Config�	get_order�get_from_id�	fill_text�get_filextension�get_default_connection�remove_filextensionc                       s�   e Zd ZdZdZdgZejdeddd�Z	ej
dd	dd
�Zejdd�Zejdd�Zej� fdd��Zdd� Zddd�Zdd� Z�  ZS )�MessageMenuz whatsapp_contacts.messaging_menuzMessaging Menuzmail.threadzwhatsapp.connectionZ
ConnectionT)�default�string�required�res.partnerZ
Recipients)r   r   ZMessage)r   zDocument Namec                    s�   t t| ��|�}d| jjv r\| jjd }| jd jdd|fgdd�}|r\dd|jgfg|d	< d
| jjv r�t| ��| jjd
 �|d< | jjd |d< |S )NZsend_tor   �phone�=�   )�limit�   r   �
recipientsZtemplate_name�message�document_name)	�superr   �default_get�env�context�search�idr   Zget_template_text)�selfr   �resr   Zpartner��	__class__� �wizard/message_menu.pyr      s    zMessageMenu.default_getc                 C   s(   | j �|�}|j|t| �jd�\}}|S )N)Zres_ids)r   �refZ_render_qweb_pdfr   r    )r!   �nameZreportZpdf_data�_r%   r%   r&   �generate_pdf#   s    zMessageMenu.generate_pdfNc                 C   s   |d u r| j S |d S d S )Nr   )r   )r!   r"   r%   r%   r&   �get_document_name)   s    zMessageMenu.get_document_namec                 C   s�   | � �  | jr| �| �� �}t| | j�}t| �}|jd|� �d� | jD ]D}| jrv| j	j
|j||| jjd d d� qH| jrH| j	�|j|� qHd S )NzWhatsapp message sent: )�body�	variablesz(slip-reference))Zcaption�filename)Z
ensure_oner   r*   r+   r
   r   r   Zmessage_postr   �
connectionZsend_pdfr   r   r   �send_message)r!   Zpdf�text�orderZ	recipientr%   r%   r&   r0   0   s    
$zMessageMenu.send_message)N)�__name__�
__module__�__qualname__�_nameZ_descriptionZ_inheritr   ZMany2oner   r/   Z	Many2manyr   �Textr   ZCharr   r   Zmodelr   r*   r+   r0   �__classcell__r%   r%   r#   r&   r      s   
r   N)Zodoor   r   r   Zodoo.exceptionsr   Z	global_pyr   r   r	   r
   r   r   r   ZTransientModelr   r%   r%   r%   r&   �<module>   s   $