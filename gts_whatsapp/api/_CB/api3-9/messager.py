a
    ʎ(g�  �                   @   s�   U d dl mZmZmZ d dlmZ d dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlZdZeed< G dd� d�ZdS )�    )�Any�Optional�Dict)�ImageNzhttps://whatapi.geektechsol.com�BASE_URLc                
   @   s�  e Zd ZdKeedd�dd�Zedd� �Zedd�d	d
�Zedd�dd�Zeedd�dd�Z	eedd�dd�Z
dd�dd�Zdd�dd�Zdd�dd�Zedd�dd�ZdLeeeeeeedd$�d%d&�ZdMeeeed(�d)d*�ZdNeeeeed+�d,d-�ZdOeeeeef  eeeef  eeedd/�d0d1�Zeeef d�d2d3�ZdPeeeeef d4�d5d6�Zejd�d7d8�Zeeejd9�d:d;��Zeeed9�d<d=��Zed�d>d?�Zeeed@�dAdB��Z dd�dCdD�Z!ee d�dEdF�Z"e#dGdH� �Z$dIdJ� Z%dS )Q�Messager�9https://webhook.site/2778607e-15e4-4af3-95a2-ee91f371be8eN)�client_secret�webhook_url�returnc                 C   s   || _ || _d | _d | _d S �N)r	   r
   �opened_chat_id�number)�selfr	   r
   � r   �api/messager.py�__init__   s    zMessager.__init__c                 C   s    t �dt| ��}|std��d S )Nz?^\+?(\d{1,3})?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$zInvalid phone number!)�re�match�str�ChildProcessError)r   Zmatchesr   r   r   �validate_number   s    zMessager.validate_number)r   r   c                 C   s0   | � |� |�d��dd�| _| j� d�| _d S )N�+� � z@c.us)r   �removeprefix�replacer   r   )r   r   r   r   r   �set_receiver   s    
zMessager.set_receiver)�messager   c                 C   s"   | � | j� | �d| j|dd��S )NZsendTextr   )�text�session)r   r   �request�get_payload)r   r   r   r   r   �send_message"   s    zMessager.send_message)�_message_idr   r   c                 C   s,   dddd�}| j |d|� �d�}| �d|�S )Nz
image/jpegz
image.jpeg�#)�mimetype�filename�urlzHere is a picture of a ��file�captionZ	sendImage)r"   r!   )r   r$   r   r*   �payloadr   r   r   �reply&   s    zMessager.reply)�
message_id�participantr   c                 C   s   | � d| j||d��S )NZsendSeen)Z	messageIdr/   �r!   r"   )r   r.   r/   r   r   r   �	send_seen+   s    zMessager.send_seen)r   c                 C   s   | j dddidd�S )Nzsessions/logout�namez	<session>F)�return_value)r!   �r   r   r   r   �logout.   s    zMessager.logoutc                 C   s   | � d| �� �S )NZstartTypingr0   r4   r   r   r   �start_typing1   s    zMessager.start_typingc                 C   s   | � d| �� �S )NZ
stopTypingr0   r4   r   r   r   �stop_typing4   s    zMessager.stop_typing)�secondsr   c                 C   s   | � �  t�|� | ��  d S r   )r6   �time�sleepr7   )r   r8   r   r   r   �typing7   s    
zMessager.typing�image�jpgr   TF�sendFile)�datar'   �filetyper+   �include_prefix�already_in_base64�	link_pathr   c                 C   sp   | � | j� |s| �|�n|}| �|�}	|r8d|	� d�nd}
| j|	|� d|� �|
� |� �d�|d�}| �||�S )Nzdata:z;base64,r   �.)r&   r'   r?   r)   )r   r   �string_to_base64�get_mimetyper"   r!   )r   r?   r'   r@   r+   rA   rB   rC   Zbase64_filer&   �prefixr,   r   r   r   �	send_file<   s    

��zMessager.send_file�document)r?   r'   r+   rB   c                 C   s   | j ||d|d|d�S )NZpdfF�rB   �rH   )r   r?   r'   r+   rB   r   r   r   �send_pdfI   s    zMessager.send_pdf)r?   r'   r+   r@   rB   c                 C   s   | j ||||d|d�S )NTrJ   rK   )r   r?   r'   r+   r@   rB   r   r   r   �
send_imageL   s    zMessager.send_image�post)�placer,   �headers�log_requestr3   �kwargsr   c           
      K   s�   |d u r| � � n|}|d u r$| �� n|}|r@td|� d|� �� tt|�}z,|t� d|� �f||d�|��}	|	��  W n. tjtj	j
tj	jtjfy�   td��Y n0 |r�|	�� S d S )Nz*[GTS-Whatsapp] Sent request with headers: z, And with payload: z/api/)rP   �jsonzFFailed to connect to whatsapp, You might be sending too many requests!)�get_headersr"   �print�getattr�requestsr   Zraise_for_status�ConnectionError�urllib3�
exceptionsZMaxRetryErrorZNewConnectionError�socketZgaierrorr   rS   )
r   rO   r,   rP   rQ   �request_typer3   rR   �func�responser   r   r   r!   O   s    
  zMessager.requestc                 C   s   | j dd�S )N�application/json�ZClientSecretzContent-Type)r	   r4   r   r   r   rT   `   s    zMessager.get_headers)�	chat_inforR   r   c                 K   s$   |r| j | jd�ni }|�|� |S )N)ZchatIdr    )r   r	   �update)r   ra   rR   r,   r   r   r   r"   c   s    
zMessager.get_payloadc                 C   s   | � �  | ��  | �| �� �S r   )r5   �start_session�text_to_qrcode_image�
get_qrcoder4   r   r   r   �authenticatei   s    zMessager.authenticate)r   r   c                 C   s:   t jdt jjddd�}|�| � |jdd� |jddd	�S )
N�   �
   �   )�versionZerror_correctionZbox_sizeZborderT)ZfitZblackZwhite)ZfillZ
back_color)�qrcodeZQRCodeZ	constantsZERROR_CORRECT_LZadd_dataZmakeZ
make_image)r   Zqrr   r   r   rd   n   s    
zMessager.text_to_qrcode_imagec                 C   s   t �| �}|�d�S )Nzutf-8)�base64Z	b64encode�decode)r   Ztext_base64r   r   r   rE   v   s    
zMessager.string_to_base64c                 C   st   | j dd�}tjtd |d�}|jdkr,dS z|�� }W n tjyN   Y dS 0 |ddikrdtd	��|�d
d�dkS )Nr_   r`   z/api/sessions/<session>/me)rP   i�  F�errorzInvalid ClientSecretz<Your client secret is invalid. Please make sure its correct.�statusz
LOGGED OUTZWORKING)r	   rW   �getr   �status_coderS   ZJSONDecodeErrorr   )r   rP   r!   �infor   r   r   �is_logged_in{   s    
zMessager.is_logged_in)�	extensionr   c                 C   s   t �d| � ��d S )Nzfile.r   )�	mimetypesZ
guess_type)rt   r   r   r   rF   �   s    zMessager.get_mimetypec              	   C   sB   dddddd�i| j ddgdddd	�gdd
�d�}| �d|� dS )z�
        Starts a whatsapp session. Each device can have a session. Session's
        initially don't have any information, But scanning a qr code will set up the session and
        insert passwords, keys, etc
        r   NZstoreTF)�enabledZfullSyncr   zsession.status)r(   ZeventsZhmacZretriesZcustomHeaders)�proxyZnowebZwebhooks�debug)r2   Zconfigzsessions/start)r
   r!   )r   r,   r   r   r   rc   �   s(    �������zMessager.start_sessionc                 C   sz   t jt� d�| �� d�}|�� }dt|�� �v rH|d dkrHt�d� q |j	dkrlt
d|j	� d|�� � ���|�� �d	�S )
Nz!/api/<session>/auth/qr?format=raw)r(   rP   rn   zUnprocessable Entity�   ��   z&Failed to fetch QR Code. Status code: z, Response: 
�value)rW   rp   r   rT   rS   �list�keysr9   r:   rq   r   )r   r^   �resultr   r   r   re   �   s    �

zMessager.get_qrcodec                 C   s   | j d| �� | �� dd�S )N�usagerp   )r,   rP   r\   )r!   r"   rT   r4   r   r   r   �requests_info�   s    zMessager.requests_infoc                 C   s   | j d| j� �i dd�S )Nzcontacts/all?session=rp   )r,   r\   )r!   r	   r4   r   r   r   �get_contacts�   s    zMessager.get_contacts)r   )r<   r=   r   TFr>   )rI   r   F)r<   r   r=   F)NNFrN   T)T)&�__name__�
__module__�__qualname__r   r   �staticmethodr   r   r#   r-   r1   r5   r6   r7   �intr;   �bytes�boolrH   rL   rM   r   r   r   r!   rT   r"   r   rf   rd   rE   rs   rF   rc   re   �propertyr�   r�   r   r   r   r   r      s<   
4"
r   )r;   r   r   r   ZPILr   rW   r9   rk   rl   ru   r   r[   rY   r   r   �__annotations__r   r   r   r   r   �<module>   s   