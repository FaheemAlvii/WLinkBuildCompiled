�
    ώ(g�  �                   �R   � d dl mZmZmZ ddlmZmZ  G d� dej                  �      Zy)�    )�fields�api�models�   )�Config�get_default_connectionc                   �   � � e Zd ZdZ ej
                  ddd��      Zej                  � fd��       Z	 ej                  d�      d� �       Z� xZS )	�SelectConnectionz"gts_whatsapp_pos.select_connectionzwhatsapp.connectionzWhatsapp ConnectionT)�string�requiredc                 �T   �� t         t        | �  |�      }t        | d�      }|r||d<   |S )N�pos_connection�
connection)�superr
   �default_getr   )�selfr   �resultr   �	__class__s       ��wizard/select_connection.pyr   zSelectConnection.default_get
   s4   �� ��'��:�6�B��+�D�2B�C�
��#-�F�<� ���    r   c                 �|   � | j                   r0t        | �      j                  d| j                   j                  �       y y )Nr   )r   r   �set�id)r   s    r   �onchange_connectionz$SelectConnection.onchange_connection   s-   � ��?�?��4�L���-�t���/A�/A�B� r   )�__name__�
__module__�__qualname__�_namer   �Many2oner   r   �modelr   �onchanger   �__classcell__)r   s   @r   r
   r
      sV   �� �0�E� ����!6�?T�_c�d�J��Y�Y�� �� �S�\�\�,��C�  �Cr   r
   N)	�odoor   r   r   �	global_pyr   r   �TransientModelr
   � r   r   �<module>r'      s"   �� $� $� 6�C�v�,�,� Cr   