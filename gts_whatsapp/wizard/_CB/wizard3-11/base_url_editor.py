�
    �T#g�  �                   �L   � d dl mZ ddlmZmZmZ  G d� dej        �  �        ZdS )�   )�Config�    )�api�fields�modelsc                   �r   � e Zd ZdZ ej        ddd� ��  �        Z ej        d�  �        d� �   �         Z	d� Z
d	S )
�BaseURLEditor�gts_whatsapp.base_url_editorzBase URLTc                 �F   � t          | �  �        �                    d�  �        S )N�base_url)r   �get��selfs    �wizard/base_url_editor.py�<lambda>zBaseURLEditor.<lambda>   s   � �RX�Y]�R^�R^�Rb�Rb�cm�Rn�Rn� �    )�string�required�defaultr   c                 ��   � | j         r^| j         �                    d�  �        r| j         �                    d�  �         t          | �  �        �                    d| j         �  �         d S d S )N�/r   )r   �endswith�removesuffixr   �setr   s    r   �onchange_base_urlzBaseURLEditor.onchange_base_url
   sh   � ��=� 	8��}�%�%�c�*�*� 0���*�*�3�/�/�/��4�L�L���Z���7�7�7�7�7�		8� 	8r   c                 �   � t          | �  �        �                    dd�  �         t          | �  �        �                    d�  �        | _        ddddd| j        d�S )	Nr   zhttps://whatapi.geektechsol.comzir.actions.act_windowzWhatsapp Base URL Editor�formr
   �new)�type�name�	view_mode�	res_model�target�res_id)r   r   r   r   �idr   s    r   �resetzBaseURLEditor.reset   s_   � ��t������%F�G�G�G��t���(�(��4�4��� ,�.��7���g�
� 
� 	
r   N)�__name__�
__module__�__qualname__�_namer   �Charr   r   �onchanger   r&   � r   r   r	   r	      sj   � � � � � �*�E��v�{�*�t�En�En�o�o�o�H��S�\�*���8� 8� ��8�
� 
� 
� 
� 
r   r	   N)�	global_pyr   �odoor   r   r   �Modelr	   r-   r   r   �<module>r1      sk   �� � � � � � � $� $� $� $� $� $� $� $� $� $�
� 
� 
� 
� 
�F�L� 
� 
� 
� 
� 
r   