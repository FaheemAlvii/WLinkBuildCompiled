o
    ̎(g  �                   @   sF   d dl mZmZmZ d dlmZ ddlmZmZ G dd� dej	�Z
dS )�    )�fields�models�api)�ValidationError�   )�Config�get_default_connectionc                   @   s   e Zd ZdZejdd� �ZdS )�PosOrderInvoicez	pos.orderc              
   C   s4   t | d�}|std��|j||dd|dddd� d S )	NZpos_connectionz*You haven't set a whatsapp connection yet!ZorderZjpgFTZ	sendImage)ZcaptionZinclude_prefixZalready_in_base64Z	link_path)r   r   Z	send_file)�selfZwhatsapp�messageZdocumentZ
connection� r   �models/pos.py�whatsapp_template_message	   s   
z)PosOrderInvoice.whatsapp_template_messageN)�__name__�
__module__�__qualname__Z_inheritr   Zmodelr   r   r   r   r   r	      s    r	   N)Zodoor   r   r   Zodoo.exceptionsr   Z	global_pyr   r   ZModelr	   r   r   r   r   �<module>   s    