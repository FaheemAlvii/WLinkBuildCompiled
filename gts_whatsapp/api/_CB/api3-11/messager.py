�
    Ύ(g�  �                   �   � U d dl mZmZmZ d dlmZ d dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlZdZeed<    G d� d�  �        ZdS )�    )�Any�Optional�Dict)�ImageNzhttps://whatapi.geektechsol.com�BASE_URLc                   �t  � e Zd Zd=dededdfd�Zed� �   �         Zdeddfd	�Zd
eddfd�Zdededdfd�Z	dededdfd�Z
d>d�Zd>d�Zd>d�Zdeddfd�Zd?dededed ed!ed"ed#eddfd$�Zd@deded ed"efd&�ZdAdeded eded"ef
d'�ZdBd)ed*eeeef                  d+eeeef                  d,ed-ed.eddfd/�Zdeeef         fd0�ZdCd1ed.edeeef         fd2�Zdej        fd3�Zededej        fd4��   �         Zededefd5��   �         Zdefd6�Zed7edefd8��   �         Z d>d9�Z!dee         fd:�Z"e#d;� �   �         Z$d<� Z%dS )D�Messager�9https://webhook.site/2778607e-15e4-4af3-95a2-ee91f371be8e�client_secret�webhook_url�returnNc                 �>   � || _         || _        d | _        d | _        d S �N)r   r   �opened_chat_id�number)�selfr   r   s      �api/messager.py�__init__zMessager.__init__   s%   � �"/��� +���-1���%)�����    c                 �l   � t          j        dt          | �  �        �  �        }|st          d�  �        �d S )Nz?^\+?(\d{1,3})?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$zInvalid phone number!)�re�match�str�ChildProcessError)r   �matchess     r   �validate_numberzMessager.validate_number   s?   � ��(�]�_b�ci�_j�_j�k�k��� 	=�#�$;�<�<�<�	=� 	=r   r   c                 �   � | �                     |�  �         |�                    d�  �        �                    dd�  �        | _        | j        � d�| _        d S )N�+� � z@c.us)r   �removeprefix�replacer   r   )r   r   s     r   �set_receiverzMessager.set_receiver   sT   � ����V�$�$�$��)�)�#�.�.�6�6�s�B�?�?���!%��3�3�3����r   �messagec                 �   � | �                     | j        �  �         | �                    d| �                    |d��  �        �  �        S )N�sendTextr    )�text�session)r   r   �request�get_payload)r   r$   s     r   �send_messagezMessager.send_message"   s?   � ����T�[�)�)�)��|�|�J��(8�(8�g�r�(8�(R�(R�S�S�Sr   �_message_idr'   c                 �n   � dddd�}| �                     |d|� ���  �        }| �                    d|�  �        S )Nz
image/jpegz
image.jpeg�#)�mimetype�filename�urlzHere is a picture of a ��file�caption�	sendImage)r*   r)   )r   r,   r'   r3   �payloads        r   �replyzMessager.reply&   sH   � �,8�l�[^�_�_��"&�"2�"2��Ff�`d�Ff�Ff�"2�"g�"g���|�|�K��1�1�1r   �
message_id�participantc                 �X   � | �                     d| �                    ||��  �        �  �        S )N�sendSeen)�	messageIdr9   �r)   r*   )r   r8   r9   s      r   �	send_seenzMessager.send_seen+   s*   � ��|�|�J��(8�(8�:�[f�(8�(g�(g�h�h�hr   c                 �6   � | �                     dddid��  �        S )Nzsessions/logout�namez	<session>F)�return_value)r)   �r   s    r   �logoutzMessager.logout.   s!   � ��|�|�-���/D�SX�|�Y�Y�Yr   c                 �R   � | �                     d| �                    �   �         �  �        S )N�startTypingr=   rB   s    r   �start_typingzMessager.start_typing1   s"   � ��|�|�M�4�+;�+;�+=�+=�>�>�>r   c                 �R   � | �                     d| �                    �   �         �  �        S )N�
stopTypingr=   rB   s    r   �stop_typingzMessager.stop_typing4   s"   � ��|�|�L�$�*:�*:�*<�*<�=�=�=r   �secondsc                 �~   � | �                     �   �          t          j        |�  �         | �                    �   �          d S r   )rF   �time�sleeprI   )r   rJ   s     r   �typingzMessager.typing7   s<   � ��������
�7�����������r   �image�jpgr    TF�sendFile�datar0   �filetyper4   �include_prefix�already_in_base64�	link_pathc                 �  � | �                     | j        �  �         |s| �                    |�  �        n|}| �                    |�  �        }	|rd|	� d�nd}
| �                    |	|� d|� �|
� |� �d�|��  �        }| �                    ||�  �        S )Nzdata:z;base64,r    �.)r/   r0   rR   r2   )r   r   �string_to_base64�get_mimetyper*   r)   )r   rR   r0   rS   r4   rT   rU   rV   �base64_filer/   �prefixr6   s               r   �	send_filezMessager.send_file<   s�   � ����T�[�)�)�)�>O�Y�4�0�0��6�6�6�UY���)�)�(�3�3��/=�E�+��+�+�+�+�2��"&�"2�"2�X�HP�E]�E]�S[�E]�E]�DJ�AY�K�AY�AY�9[� 9[�dk� #3� #m� #m�� �|�|�I�w�/�/�/r   �documentc                 �8   � | �                     ||d|d|��  �        S )N�pdfF�rU   �r]   )r   rR   r0   r4   rU   s        r   �send_pdfzMessager.send_pdfI   s!   � ��~�~�d�H�e�W�e�Wh�~�i�i�ir   c                 �8   � | �                     ||||d|��  �        S )NTra   rb   )r   rR   r0   r4   rS   rU   s         r   �
send_imagezMessager.send_imageL   s!   � ��~�~�d�H�h���Yj�~�k�k�kr   �post�placer6   �headers�log_requestrA   �kwargsc                 ��  � |�| �                     �   �         n|}|�| �                    �   �         n|}|rt          d|� d|� ��  �         t          t          |�  �        }	  |t
          � d|� �f||d�|��}	|	�                    �   �          nN# t          j        t          j	        j
        t          j	        j        t          j        f$ r t          d�  �        �w xY w|r|	�                    �   �         S d S )Nz*[GTS-Whatsapp] Sent request with headers: z, And with payload: z/api/)rh   �jsonzFFailed to connect to whatsapp, You might be sending too many requests!)�get_headersr*   �print�getattr�requestsr   �raise_for_status�ConnectionError�urllib3�
exceptions�MaxRetryError�NewConnectionError�socket�gaierrorr   rl   )
r   rg   r6   rh   ri   �request_typerA   rj   �func�responses
             r   r)   zMessager.requestO   s+  � �(/��$�"�"�$�$�$�W��(/��$�"�"�$�$�$�W��� 	g��e�w�e�e�\c�e�e�f�f�f��x��.�.��	n�*.�$�(�/H�/H��/H�/H�*r�RY�`g�*r�*r�kq�*r�*r�H��%�%�'�'�'�'���(�'�*<�*J�G�L^�Lq�sy�  tC�  D� 	n� 	n� 	n�#�$l�m�m�m�	n���� � 	#��=�=�?�?�"�	#� 	#s   �*B	 �	ACc                 �   � | j         dd�S )N�application/json��ClientSecretzContent-Type)r   rB   s    r   rm   zMessager.get_headers`   s   � � $� 2�DV�W�W�Wr   �	chat_infoc                 �V   � |r| j         | j        d�ni }|�                    |�  �         |S )N)�chatIdr(   )r   r   �update)r   r�   rj   r6   s       r   r*   zMessager.get_payloadc   s7   � �dm�"u�T�-@�T�M_�"`�"`�"`�su�����v�����r   c                 �   � | �                     �   �          | �                    �   �          | �                    | �                    �   �         �  �        S r   )rC   �start_session�text_to_qrcode_image�
get_qrcoderB   s    r   �authenticatezMessager.authenticatei   s?   � ��������������(�(����):�):�;�;�;r   c                 ��   � t          j        dt           j        j        dd��  �        }|�                    | �  �         |�                    d��  �         |�                    dd�	�  �        S )
N�   �
   �   )�version�error_correction�box_size�borderT)�fit�black�white)�fill�
back_color)�qrcode�QRCode�	constants�ERROR_CORRECT_L�add_data�make�
make_image)r'   �qrs     r   r�   zMessager.text_to_qrcode_imagen   s^   � ��]�1�v�7G�7W�bd�mn�o�o�o��
���D����
���D������}�}�'�g�}�>�>�>r   c                 �T   � t          j        | �  �        }|�                    d�  �        S )Nzutf-8)�base64�	b64encode�decode)r'   �text_base64s     r   rY   zMessager.string_to_base64v   s&   � ��&�t�,�,���!�!�'�*�*�*r   c                 �&  � | j         dd�}t          j        t          dz   |��  �        }|j        dk    rdS 	 |�                    �   �         }n# t          j        $ r Y dS w xY w|ddik    rt          d	�  �        �|�                    d
d�  �        dk    S )Nr}   r~   z/api/sessions/<session>/me)rh   i�  F�errorzInvalid ClientSecretz<Your client secret is invalid. Please make sure its correct.�statusz
LOGGED OUT�WORKING)r   rp   �getr   �status_coderl   �JSONDecodeErrorr   )r   rh   r)   �infos       r   �is_logged_inzMessager.is_logged_in{   s�   � �#'�#5�GY�Z�Z���,�x�*G�G�QX�Y�Y�Y����#�%�%��5�	��<�<�>�>�D�D���'� 	� 	� 	��5�5�	���� �G�3�4�4�4�#�$b�c�c�c��x�x��,�/�/�9�<�<s   �A �A�A�	extensionc                 �<   � t          j        d| � ��  �        d         S )Nzfile.r   )�	mimetypes�
guess_type)r�   s    r   rZ   zMessager.get_mimetype�   s!   � ��#�$7�I�$7�$7�8�8��;�;r   c           	      �l   � dddddd�i| j         ddgdddd	�gdd
�d�}| �                    d|�  �         dS )z�
        Starts a whatsapp session. Each device can have a session. Session's
        initially don't have any information, But scanning a qr code will set up the session and
        insert passwords, keys, etc
        r    N�storeTF)�enabled�fullSyncr$   zsession.status)r1   �events�hmac�retries�customHeaders)�proxy�noweb�webhooks�debug)r@   �configzsessions/start)r   r)   )r   r6   s     r   r�   zMessager.start_session�   s�   � � ���#'�$)�� ��  $�/�%�,�#� !%�#'�)-�	� 	�� �)� �#
� #
��4 	���%�w�/�/�/�/�/r   c                 ��  � 	 t          j        t          � d�| �                    �   �         ��  �        }|�                    �   �         }dt          |�                    �   �         �  �        v r!|d         dk    rt          j        d�  �         ��|j	        dk    r,t          d|j	        � d	|�                    �   �         � ��  �        �|�                    �   �         �                    d
�  �        S )NTz!/api/<session>/auth/qr?format=raw)r1   rh   r�   zUnprocessable Entity�   ��   z&Failed to fetch QR Code. Status code: z, Response: 
�value)rp   r�   r   rm   rl   �list�keysrL   rM   r�   r   )r   r{   �results      r   r�   zMessager.get_qrcode�   s  � �	0�*2�,��B�B�B��(�(�*�*�+� +� +�H�
 &.�]�]�_�_�F��$�v�{�{�}�}�-�-�-�-�&��/�E[�2[�2[��
�1������#�s�*�*�'�  )G�QY�Qe�  )G�  )G�u}�  vC�  vC�  vE�  vE�  )G�  )G�  H�  H�  H��=�=�?�?�&�&�w�/�/�/r   c                 �|   � | �                     d| �                    �   �         | �                    �   �         d��  �        S )N�usager�   )r6   rh   ry   )r)   r*   rm   rB   s    r   �requests_infozMessager.requests_info�   s5   � ��|�|�G�T�-=�-=�-?�-?��IY�IY�I[�I[�jo�|�p�p�pr   c                 �B   � | �                     d| j        � �i d��  �        S )Nzcontacts/all?session=r�   )r6   ry   )r)   r   rB   s    r   �get_contactszMessager.get_contacts�   s(   � ��|�|�H�D�4F�H�H�RT�ch�|�i�i�ir   )r
   )r   N)rO   rP   r    TFrQ   )r^   r    F)rO   r    rP   F)NNFrf   T)T)&�__name__�
__module__�__qualname__r   r   �staticmethodr   r#   r+   r7   r>   rC   rF   rI   �intrN   �bytes�boolr]   rc   re   r   r   r   r)   rm   r*   r   r�   r�   rY   r�   rZ   r�   r�   �propertyr�   r�   � r   r   r	   r	      sZ  � � � � � �*� *�c� *�� *�  C� *� *� *� *� �=� =� �\�=�
4�3� 4�4� 4� 4� 4� 4�
T�C� T�D� T� T� T� T�2�� 2�C� 2�D� 2� 2� 2� 2�
i�C� i�c� i�d� i� i� i� i�Z� Z� Z� Z�?� ?� ?� ?�>� >� >� >��c� �d� � � � �
0� 0�e� 0�s� 0�� 0�^a� 0�x|� 0�  Y]� 0�  ru� 0�  GK� 0� 0� 0� 0�j� j�U� j�c� j�� j�fj� j� j� j� j�l� l�u� l�� l�� l�\_� l�  }A� l� l� l� l�#� #�S� #�8�D��c��N�+C� #�U]�^b�cf�hk�ck�^l�Um� #�  DH� #�  uy� #�  LO� #�  TX� #� #� #� #�"X�T�#�s�(�^� X� X� X� X�� �T� �C� �D��c��N� � � � �<�e�k� <� <� <� <�
 �?�3� ?�5�;� ?� ?� ?� �\�?� �+�u� +�� +� +� +� �\�+�=�d� =� =� =� =�" �<�� <�� <� <� <� �\�<� 0�  0�  0�  0�D0�H�S�M� 0� 0� 0� 0�$ �q� q� �X�q�j� j� j� j� jr   r	   )rN   r   r   r   �PILr   rp   rL   r�   r�   r�   r   rw   rs   r   r   �__annotations__r	   r�   r   r   �<module>r�      s�   �� &� &� &� &� &� &� &� &� &� &� &� � � � � � � ���� ���� ���� ���� � � � � 	�	�	�	� ���� ���� 2��#� 1� 1� 1�yj� yj� yj� yj� yj� yj� yj� yj� yj� yjr   