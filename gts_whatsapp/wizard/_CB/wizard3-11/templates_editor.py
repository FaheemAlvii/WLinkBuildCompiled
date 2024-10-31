�
    �T#gG  �                   �P   � d dl mZmZ ddlmZmZmZ  G d� dej        �  �        ZdS )�   )�Config�
get_reopen�    )�api�fields�modelsc                   ��   � e Zd ZdZd� Z ej        eddd��  �        Z ej        d��  �        Z	 e
j        d	�  �        d
� �   �         Z e
j        d�  �        d� �   �         Zd� ZdS )�TemplatesEditorzgts_whatsapp.templates_editorc                 �   �� d� ��fd�t          | �  �        �                    d�  �        �                    �   �         D �   �         S )Nc                 �z   � | �                     dd�  �        �                     dd�  �        �                    �   �         S )Nzstock.action_report_� �_� )�replace�
capitalize)�template_ids    �wizard/templates_editor.py�<lambda>z8TemplatesEditor.get_template_selection.<locals>.<lambda>	   s6   � �{�':�':�;Q�SU�'V�'V�'^�'^�_b�dg�'h�'h�'s�'s�'u�'u� �    c                 �*   �� g | ]}| �|�  �        f��S � r   )�.0r   �humanifys     �r   �
<listcomp>z:TemplatesEditor.get_template_selection.<locals>.<listcomp>
   s(   �� �r�r�r���h�h�{�3�3�4�r�r�rr   �templates_text)r   �get�keys)�selfr   s    @r   �get_template_selectionz&TemplatesEditor.get_template_selection   sF   �� �u�u��r�r�r�r��t���HX�HX�Yi�Hj�Hj�Ho�Ho�Hq�Hq�r�r�r�rr   zTemplate NameT�sales_quotations)�string�required�defaultzTemplate Text)r!   �templatec                 �p   � | j         r.t          | �  �        �                    | j         �  �        | _        d S d S �N)r$   r   �get_template_text�template_text�r   s    r   �onchange_templatez!TemplatesEditor.onchange_template   s=   � ��=� 	O�!'����!?�!?���!N�!N�D����	O� 	Or   r(   c                 �r   � | j         r/t          | �  �        �                    | j        | j         �  �         d S d S r&   )r(   r   �set_template_textr$   r)   s    r   �onchange_template_textz&TemplatesEditor.onchange_template_text   sA   � ��� 	N��4�L�L�*�*�4�=�$�:L�M�M�M�M�M�	N� 	Nr   c                 ��   � t          | �  �        �                    dd �  �         t          | �  �         t          | �  �        �                    | j        �  �        | _        t          | d�  �        S )Nr   zWhatsapp Templates Editor)r   �setr'   r$   r(   r   r)   s    r   �resetzTemplatesEditor.reset   s[   � ��t�����)�4�0�0�0��t���� $�D�\�\�;�;�D�M�J�J����$� ;�<�<�<r   N)�__name__�
__module__�__qualname__�_namer   r   �	Selectionr$   �Textr(   r   �onchanger*   r-   r0   r   r   r   r
   r
      s�   � � � � � �+�E�s� s� s�  �v�� 6��Y]�gy�z�z�z�H��F�K��7�7�7�M��S�\�*���O� O� ��O� �S�\�/�"�"�N� N� #�"�N�	=� 	=� 	=� 	=� 	=r   r
   N)	�	global_pyr   r   �odoor   r   r   �TransientModelr
   r   r   r   �<module>r;      sr   �� *� *� *� *� *� *� *� *� $� $� $� $� $� $� $� $� $� $�=� =� =� =� =�f�+� =� =� =� =� =r   