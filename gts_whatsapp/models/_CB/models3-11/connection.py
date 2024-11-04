�
    Ύ(gd  �                   ��   � d dl mZ d dlmZmZmZ d dlmZ ddlmZ ddl	m
Z
 d dlZd dlZd� Z e ej        d	d
d�  �        �  �        Z G d� dej        �  �        Z G d� dej        �  �        ZdS )�    )�Image)�api�fields�models)�ValidationError�   )�Messager)�ConfigNc                 ��   � t          j        �   �         }| �                    |d�  �         |�                    d�  �         t	          j        |�                    �   �         �  �        S )N�JPEGr   )�io�BytesIO�save�seek�base64�	b64encode�read)�image�fs     �models/connection.py�encode_image_to_base64r   
   sI   � �
�
���A�	�J�J�q�&�����F�F�1�I�I�I���A�F�F�H�H�%�%�%�    �RGB)�   r   )��   r   r   c                   �b   � � e Zd ZdZdZ ej        d��  �        Zej	        � fd��   �         Z
� xZS )�	LoginMenu�whatsapp.login_menuz
Login MenuzQR Code)�stringc                 �   �� t          t          | �  �        �                    |�  �        }d| j        j        v r| j        j        d         }||d<   |S )N�qrcode)�superr   �default_get�env�context)�selfr   �resr!   �	__class__s       �r   r#   zLoginMenu.default_get   sM   �� ��I�t�$�$�0�0��8�8���t�x�'�'�'��X�%�h�/�F�"�C��M��
r   )�__name__�
__module__�__qualname__�_name�_descriptionr   r   r!   r   �modelr#   �__classcell__)r(   s   @r   r   r      sb   �� � � � � �!�E��L��V�\��+�+�+�F��Y�� � � � �Y�� � � � r   r   c                   �j  � e Zd ZdZdZdgZ ej        dd��  �        Z ej        dd��  �        Z	 ej
        ddd�	�  �        Z ej
        d
dd�	�  �        Z ej        ddd�	�  �        Zd� Zd� Zd� Zd� Zd� Zd� Zd'dededededdf
d�Zed� �   �         Z	 	 	 	 	 	 d(dededed!eded"ed#ed$efd%�Zd&� ZdS ))�
Connectionzwhatsapp.connectionzWhatsapp Connectionzmail.thread�NameT)r   �requiredzAPI Key�Active)r   �defaultr3   z	Logged InFzRequests Left Todayr   c                 �V   � t          | �  �        �                    d| j        �  �         d S )N�default_connection)r
   �set�id�r&   s    r   �set_as_default_connectionz$Connection.set_as_default_connection0   s'   � ��t�����-�t�w�7�7�7�7�7r   c                 �  � | D ]|}|�                     �   �          |j        rt          d�  �        �|j        s�4t	          |j        �  �        }|�                    �   �         }t          |�  �        }dddd| j        |d�d�c S d S )NzAlready logged in!zir.actions.act_window�formr   �new)�orderr!   )�type�	view_mode�	res_model�targetr%   )�check_status�	logged_inr   �client_secretr	   �authenticater   r9   )r&   �record�messager�pillow_image�base64_images        r   �loginzConnection.login3   s�   � �� 	� 	�F����!�!�!��� <�%�&:�;�;�;��'� ���� 4�5�5�H�#�0�0�2�2�L�1�,�?�?�L� 0�#�2��%)�W��E�E�� � � � �	� 	r   c                 �n   � t          | j        �  �        j        }|�                    dd�  �        | _        d S )N�remaining_requestsr   )r	   rF   �requests_info�get�requests_left)r&   rO   s     r   �check_left_requestszConnection.check_left_requestsJ   s4   � � ��!3�4�4�B��*�.�.�/C�Q�G�G����r   c                 ��   � 	 t          | j        �  �        �                    �   �         | _        | �                    �   �          d S # t
          $ r }| �                    |�  �         Y d }~d S d }~ww xY w�N)r	   rF   �is_logged_inrE   rR   �ChildProcessError�handle_exception)r&   �es     r   rD   zConnection.check_statusN   s�   � �	%�%�d�&8�9�9�F�F�H�H�D�N��$�$�&�&�&�&�&�� � 	%� 	%� 	%��!�!�!�$�$�$�$�$�$�$�$�$�����	%���s   �?A �
A-�A(�(A-c                 �R   � t          | j        �  �        �                    �   �          d S rT   )r	   rF   �logoutr:   s    r   rZ   zConnection.logoutU   s%   � ���#�$�$�+�+�-�-�-�-�-r   c                 ��   � 	 t          | j        �  �        }|�                    |�  �         |�                    |�  �         d S # t          $ r }| �                    |�  �         Y d }~d S d }~ww xY wrT   )r	   rF   �set_receiver�send_messagerV   rW   )r&   �to_phone_number�messagerI   rX   s        r   r]   zConnection.send_messageX   s�   � �	%��� 2�3�3�H��!�!�/�2�2�2��!�!�'�*�*�*�*�*�� � 	%� 	%� 	%��!�!�!�$�$�$�$�$�$�$�$�$�����	%���s   �>A �
A,�A'�'A,�document� r^   �data�filename�caption�returnNc                 �
  � | �                     �   �          	 t          | j        �  �        }|�                    |�  �         |�                    |||�  �         d S # t
          $ r }| �                    |�  �         Y d }~d S d }~ww xY wrT   )�
ensure_oner	   rF   r\   �send_pdfrV   rW   )r&   r^   rb   rc   rd   rI   rX   s          r   rh   zConnection.send_pdf`   s�   � �������	%��� 2�3�3�H��!�!�/�2�2�2����d�H�g�6�6�6�6�6�� � 	%� 	%� 	%��!�!�!�$�$�$�$�$�$�$�$�$�����	%���s   �A A �
B�"A=�=Bc                 �f   � t          | t          �  �        rt          t          | �  �        �  �        �� rT   )�
isinstancerV   r   �str)rX   s    r   rW   zConnection.handle_exceptionj   s,   � ��a�*�+�+� 	�!�#�a�&�&�)�)�)�r   r   �jpg�sendFile�filetype�include_prefix�already_in_base64�	link_pathc	           	      ��   � 	 t          | j        �  �        }	|	�                    |�  �         |	�                    |||||||�  �         d S # t          $ r }
| �                    |
�  �         Y d }
~
d S d }
~
ww xY wrT   )r	   rF   r\   �	send_filerV   rW   )r&   r^   rb   rc   rn   rd   ro   rp   rq   rI   rX   s              r   rs   zConnection.send_fileq   s�   � �	%��� 2�3�3�H��!�!�/�2�2�2����t�X�x��.�Rc�en�o�o�o�o�o�� � 	%� 	%� 	%��!�!�!�$�$�$�$�$�$�$�$�$�����	%���s   �AA �
A2�A-�-A2c                 �   � 	 t          | j        �  �        �                    �   �         S # t          $ r }| �                    |�  �         Y d }~d S d }~ww xY wrT   )r	   rF   �get_contactsrV   rW   )r&   �	exceptionrX   s      r   ru   zConnection.get_contacts�   si   � �	%��D�.�/�/�<�<�>�>�>�� � 	%� 	%� 	%��!�!�!�$�$�$�$�$�$�$�$�$�����	%���s   �%( �
A�A�A)r`   ra   )r   rl   ra   TFrm   )r)   r*   r+   r,   r-   �_inheritr   �Char�namerF   �Boolean�activerE   �IntegerrQ   r;   rL   rR   rD   rZ   r]   rk   �bytesrh   �staticmethodrW   �boolrs   ru   � r   r   r1   r1   %   s�  � � � � � �!�E�(�L���H��6�;�f�t�4�4�4�D��F�K�y�4�@�@�@�M��V�^�8�T�D�I�I�I�F����k�5�4�P�P�P�I�"�F�N�*?��UY�Z�Z�Z�M�8� 8� 8�� � �.H� H� H�%� %� %�.� .� .�%� %� %�%� %�� %�5� %�C� %�_b� %�lp� %� %� %� %� �� � �\�� #*�"'�!#�)-�,1�#-�%� %�#&�%��%�  �%�  �	%�
 �%� #'�%� &*�%� !�%� %� %� %�$%� %� %� %� %r   r1   )�PILr   �odoor   r   r   �odoo.exceptionsr   r	   �	global_pyr
   r   r   r   r>   �BLANK_IMAGE�TransientModelr   �Modelr1   r�   r   r   �<module>r�      s  �� � � � � � � $� $� $� $� $� $� $� $� $� $� +� +� +� +� +� +� � � � � � � � � � � � � ���� 	�	�	�	�&� &� &� %�$�Y�U�Y�u�f�o�%N�%N�O�O��� � � � ��%� � � �"b%� b%� b%� b%� b%��� b%� b%� b%� b%� b%r   