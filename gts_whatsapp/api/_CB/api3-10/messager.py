o
    ̎(g�  �                   @   s�   U d dl mZmZmZ d dlmZ d dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlZdZeed< G dd� d�ZdS )�    )�Any�Optional�Dict)�ImageNzhttps://whatapi.geektechsol.com�BASE_URLc                   @   s   e Zd ZdVdededdfdd�Zedd	� �Zd
eddfdd�Zdeddfdd�Zdededdfdd�Z	dededdfdd�Z
dWdd�ZdWdd�ZdWdd�Zdeddfdd �ZdXd'ed(ed)ed*ed+ed,ed-eddfd.d/�ZdYd'ed(ed*ed,efd1d2�ZdZd'ed(ed*ed)ed,ef
d3d4�Zd[d6ed7eeeef  d8eeeef  d9ed:ed;eddfd<d=�Zdeeef fd>d?�Zd\d@ed;edeeef fdAdB�ZdejfdCdD�ZededejfdEdF��ZededefdGdH��ZdefdIdJ�ZedKedefdLdM��Z dWdNdO�Z!dee fdPdQ�Z"e#dRdS� �Z$dTdU� Z%dS )]�Messager�9https://webhook.site/2778607e-15e4-4af3-95a2-ee91f371be8e�client_secret�webhook_url�returnNc                 C   s   || _ || _d | _d | _d S �N)r	   r
   �opened_chat_id�number)�selfr	   r
   � r   �api/messager.py�__init__   s   
zMessager.__init__c                 C   s    t �dt| ��}|std��d S )Nz?^\+?(\d{1,3})?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$zInvalid phone number!)�re�match�str�ChildProcessError)r   Zmatchesr   r   r   �validate_number   s   �zMessager.validate_numberr   c                 C   s0   | � |� |�d��dd�| _| j� d�| _d S )N�+� � z@c.us)r   �removeprefix�replacer   r   )r   r   r   r   r   �set_receiver   s   
zMessager.set_receiver�messagec                 C   s"   | � | j� | �d| j|dd��S )NZsendTextr   )�text�session)r   r   �request�get_payload)r   r   r   r   r   �send_message"   s   zMessager.send_message�_message_idr   c                 C   s,   dddd�}| j |d|� �d�}| �d|�S )Nz
image/jpegz
image.jpeg�#)�mimetype�filename�urlzHere is a picture of a ��file�captionZ	sendImage)r"   r!   )r   r$   r   r*   �payloadr   r   r   �reply&   s   zMessager.reply�
message_id�participantc                 C   s   | � d| j||d��S )NZsendSeen)Z	messageIdr/   �r!   r"   )r   r.   r/   r   r   r   �	send_seen+   �   zMessager.send_seenc                 C   s   | j dddidd�S )Nzsessions/logout�namez	<session>F)�return_value)r!   �r   r   r   r   �logout.   s   zMessager.logoutc                 C   �   | � d| �� �S )NZstartTypingr0   r5   r   r   r   �start_typing1   �   zMessager.start_typingc                 C   r7   )NZ
stopTypingr0   r5   r   r   r   �stop_typing4   r9   zMessager.stop_typing�secondsc                 C   s   | � �  t�|� | ��  d S r   )r8   �time�sleepr:   )r   r;   r   r   r   �typing7   s   
zMessager.typing�image�jpgr   TF�sendFile�datar'   �filetyper+   �include_prefix�already_in_base64�	link_pathc                 C   sp   | � | j� |s| �|�n|}| �|�}	|rd|	� d�nd}
| j|	|� d|� �|
� |� �d�|d�}| �||�S )Nzdata:z;base64,r   �.)r&   r'   rB   r)   )r   r   �string_to_base64�get_mimetyper"   r!   )r   rB   r'   rC   r+   rD   rE   rF   Zbase64_filer&   �prefixr,   r   r   r   �	send_file<   s   

��zMessager.send_file�documentc                 C   s   | j ||d|d|d�S )NZpdfF�rE   �rK   )r   rB   r'   r+   rE   r   r   r   �send_pdfI   r2   zMessager.send_pdfc                 C   s   | j ||||d|d�S )NTrM   rN   )r   rB   r'   r+   rC   rE   r   r   r   �
send_imageL   r2   zMessager.send_image�post�placer,   �headers�log_requestr4   �kwargsc           
      K   s�   |d u r| � � n|}|d u r| �� n|}|r td|� d|� �� tt|�}z|t� d|� �f||d�|��}	|	��  W n tjtj	j
tj	jtjfyP   td��w |rW|	�� S d S )Nz*[GTS-Whatsapp] Sent request with headers: z, And with payload: z/api/)rS   �jsonzFFailed to connect to whatsapp, You might be sending too many requests!)�get_headersr"   �print�getattr�requestsr   Zraise_for_status�ConnectionError�urllib3�
exceptionsZMaxRetryErrorZNewConnectionError�socketZgaierrorr   rV   )
r   rR   r,   rS   rT   �request_typer4   rU   �func�responser   r   r   r!   O   s   
  ��zMessager.requestc                 C   s   | j dd�S )N�application/json�ZClientSecretzContent-Type)r	   r5   r   r   r   rW   `   s   zMessager.get_headers�	chat_infoc                 K   s$   |r	| j | jd�ni }|�|� |S )N)ZchatIdr    )r   r	   �update)r   rd   rU   r,   r   r   r   r"   c   s   
zMessager.get_payloadc                 C   s   | � �  | ��  | �| �� �S r   )r6   �start_session�text_to_qrcode_image�
get_qrcoder5   r   r   r   �authenticatei   s   zMessager.authenticatec                 C   s:   t jdt jjddd�}|�| � |jdd� |jddd	�S )
N�   �
   �   )�versionZerror_correctionZbox_sizeZborderT)ZfitZblackZwhite)ZfillZ
back_color)�qrcodeZQRCodeZ	constantsZERROR_CORRECT_LZadd_dataZmakeZ
make_image)r   Zqrr   r   r   rg   n   s   
zMessager.text_to_qrcode_imagec                 C   s   t �| �}|�d�S )Nzutf-8)�base64Z	b64encode�decode)r   Ztext_base64r   r   r   rH   v   s   

zMessager.string_to_base64c                 C   st   | j dd�}tjtd |d�}|jdkrdS z|�� }W n tjy'   Y dS w |ddikr2td	��|�d
d�dkS )Nrb   rc   z/api/sessions/<session>/me)rS   i�  F�errorzInvalid ClientSecretz<Your client secret is invalid. Please make sure its correct.Zstatusz
LOGGED OUTZWORKING)r	   rZ   �getr   �status_coderV   ZJSONDecodeErrorr   )r   rS   r!   �infor   r   r   �is_logged_in{   s   
�zMessager.is_logged_in�	extensionc                 C   s   t �d| � ��d S )Nzfile.r   )�	mimetypesZ
guess_type)rv   r   r   r   rI   �   s   zMessager.get_mimetypec              	   C   sB   dddddd�i| j ddgdddd	�gdd
�d�}| �d|� dS )z�
        Starts a whatsapp session. Each device can have a session. Session's
        initially don't have any information, But scanning a qr code will set up the session and
        insert passwords, keys, etc
        r   NZstoreTF)�enabledZfullSyncr   zsession.status)r(   ZeventsZhmacZretriesZcustomHeaders)�proxyZnowebZwebhooks�debug)r3   Zconfigzsessions/start)r
   r!   )r   r,   r   r   r   rf   �   s(   �������zMessager.start_sessionc                 C   s|   	 t jt� d�| �� d�}|�� }dt|�� �v r%|d dkr%t�d� q |j	dkr7t
d|j	� d	|�� � ���|�� �d
�S )NTz!/api/<session>/auth/qr?format=raw)r(   rS   rq   zUnprocessable Entity�   ��   z&Failed to fetch QR Code. Status code: z, Response: 
�value)rZ   rr   r   rW   rV   �list�keysr<   r=   rs   r   )r   ra   �resultr   r   r   rh   �   s   �

zMessager.get_qrcodec                 C   s   | j d| �� | �� dd�S )N�usagerr   )r,   rS   r_   )r!   r"   rW   r5   r   r   r   �requests_info�   s   zMessager.requests_infoc                 C   s   | j d| j� �i dd�S )Nzcontacts/all?session=rr   )r,   r_   )r!   r	   r5   r   r   r   �get_contacts�   s   zMessager.get_contacts)r   )r   N)r?   r@   r   TFrA   )rL   r   F)r?   r   r@   F)NNFrQ   T)T)&�__name__�
__module__�__qualname__r   r   �staticmethodr   r   r#   r-   r1   r6   r8   r:   �intr>   �bytes�boolrK   rO   rP   r   r   r   r!   rW   r"   r   ri   rg   rH   ru   rI   rf   rh   �propertyr�   r�   r   r   r   r   r      s>    



, @ 
"
r   )r>   r   r   r   ZPILr   rZ   r<   rn   ro   rw   r   r^   r\   r   r   �__annotations__r   r   r   r   r   �<module>   s    