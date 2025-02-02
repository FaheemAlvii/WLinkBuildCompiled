�
    ͎(g  �                   �\   � d dl mZmZmZ d dlmZ ddlmZmZ  G d� dej	        �  �        Z
dS )�    )�fields�models�api)�ValidationError�   )�Config�get_default_connectionc                   �2   � e Zd ZdZej        d� �   �         ZdS )�PosOrderInvoicez	pos.orderc           
      �   � t          | d�  �        }|st          d�  �        �|�                    ||dd|ddd��  �         d S )	N�pos_connectionz*You haven't set a whatsapp connection yet!�order�jpgFT�	sendImage)�caption�include_prefix�already_in_base64�	link_path)r	   r   �	send_file)�self�whatsapp�message�document�
connections        �models/pos.py�whatsapp_template_messagez)PosOrderInvoice.whatsapp_template_message	   sk   � �+�D�2B�C�C�
�� 	P�!�"N�O�O�O����X�x��%��af�z~�  KV��  	W�  	W�  	W�  	W�  	W�    N)�__name__�
__module__�__qualname__�_inheritr   �modelr   � r   r   r   r      s9   � � � � � ��H��Y�W� W� �Y�W� W� Wr   r   N)�odoor   r   r   �odoo.exceptionsr   �	global_pyr   r	   �Modelr   r#   r   r   �<module>r(      s�   �� $� $� $� $� $� $� $� $� $� $� +� +� +� +� +� +� 6� 6� 6� 6� 6� 6� 6� 6�
W� 
W� 
W� 
W� 
W�f�l� 
W� 
W� 
W� 
W� 
Wr   