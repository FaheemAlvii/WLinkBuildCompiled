�
    ώ(g�  �                   �N   � d dl mZ ddlmZmZmZ  G d� dej                  �      Zy)�   )�Config�    )�api�fields�modelsc                   �r   � e Zd ZdZ ej
                  ddd� ��      Z ej                  d�      d� �       Z	d� Z
y	)
�BaseURLEditor�gts_whatsapp.base_url_editorzBase URLTc                 �6   � t        | �      j                  d�      S )N�base_url)r   �get��selfs    �wizard/base_url_editor.py�<lambda>zBaseURLEditor.<lambda>   s   � �RX�Y]�R^�Rb�Rb�cm�Rn� �    )�string�required�defaultr   c                 ��   � | j                   r\| j                   j                  d�      r| j                   j                  d�       t        | �      j	                  d| j                   �       y y )N�/r   )r   �endswith�removesuffixr   �setr   s    r   �onchange_base_urlzBaseURLEditor.onchange_base_url
   sJ   � ��=�=��}�}�%�%�c�*����*�*�3�/��4�L���Z����7�	 r   c                 �   � t        | �      j                  dd�       t        | �      j                  d�      | _        ddddd| j                  d�S )	Nr   zhttps://whatapi.geektechsol.comzir.actions.act_windowzWhatsapp Base URL Editor�formr
   �new)�type�name�	view_mode�	res_model�target�res_id)r   r   r   r   �idr   s    r   �resetzBaseURLEditor.reset   sO   � ��t�����%F�G��t��(�(��4��� ,�.��7���g�g�
� 	
r   N)�__name__�
__module__�__qualname__�_namer   �Charr   r   �onchanger   r&   � r   r   r	   r	      s>   � �*�E��v�{�{�*�t�En�o�H��S�\�\�*��8� �8�
r   r	   N)�	global_pyr   �odoor   r   r   �Modelr	   r-   r   r   �<module>r1      s   �� � $� $�
�F�L�L� 
r   