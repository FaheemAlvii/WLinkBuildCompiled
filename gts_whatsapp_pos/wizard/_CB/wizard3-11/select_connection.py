�
    ͎(g�  �                   �P   � d dl mZmZmZ ddlmZmZ  G d� dej        �  �        ZdS )�    )�fields�api�models�   )�Config�get_default_connectionc                   �   � � e Zd ZdZ ej        ddd��  �        Zej        � fd��   �         Z	 ej
        d�  �        d� �   �         Z� xZS )	�SelectConnectionz"gts_whatsapp_pos.select_connectionzwhatsapp.connectionzWhatsapp ConnectionT)�string�requiredc                 �   �� t          t          | �  �        �                    |�  �        }t          | d�  �        }|r||d<   |S )N�pos_connection�
connection)�superr
   �default_getr   )�selfr   �resultr   �	__class__s       ��wizard/select_connection.pyr   zSelectConnection.default_get
   sH   �� ��'��.�.�:�:�6�B�B��+�D�2B�C�C�
�� 	.�#-�F�<� ���    r   c                 �r   � | j         r/t          | �  �        �                    d| j         j        �  �         d S d S )Nr   )r   r   �set�id)r   s    r   �onchange_connectionz$SelectConnection.onchange_connection   sA   � ��?� 	C��4�L�L���-�t��/A�B�B�B�B�B�	C� 	Cr   )�__name__�
__module__�__qualname__�_namer   �Many2oner   r   �modelr   �onchanger   �__classcell__)r   s   @r   r
   r
      s�   �� � � � � �0�E� ���!6�?T�_c�d�d�d�J��Y�� � � � �Y�� �S�\�,���C� C�  ��C� C� C� C� Cr   r
   N)	�odoor   r   r   �	global_pyr   r   �TransientModelr
   � r   r   �<module>r'      s|   �� $� $� $� $� $� $� $� $� $� $� 6� 6� 6� 6� 6� 6� 6� 6�C� C� C� C� C�v�,� C� C� C� C� Cr   