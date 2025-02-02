�
    ώ(g  �                   �^   � d dl mZmZmZ d dlmZ ddlmZmZ  G d� dej                  �      Z
y)�    )�fields�models�api)�ValidationError�   )�Config�get_default_connectionc                   �4   � e Zd ZdZej
                  d� �       Zy)�PosOrderInvoicez	pos.orderc           
      �h   � t        | d�      }|st        d�      �|j                  ||dd|ddd��       y )	N�pos_connectionz*You haven't set a whatsapp connection yet!�order�jpgFT�	sendImage)�caption�include_prefix�already_in_base64�	link_path)r	   r   �	send_file)�self�whatsapp�message�document�
connections        �models/pos.py�whatsapp_template_messagez)PosOrderInvoice.whatsapp_template_message	   sG   � �+�D�2B�C�
��!�"N�O�O����X�x��%��af�z~�  KV��  	W�    N)�__name__�
__module__�__qualname__�_inheritr   �modelr   � r   r   r   r      s   � ��H��Y�Y�W� �Wr   r   N)�odoor   r   r   �odoo.exceptionsr   �	global_pyr   r	   �Modelr   r#   r   r   �<module>r(      s#   �� $� $� +� 6�
W�f�l�l� 
Wr   