�
    ώ(g�  �                   �   � U d dl mZmZmZ d dlmZ d dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlZdZeed<    G d� d�      Zy)�    )�Any�Optional�Dict)�ImageNzhttps://whatapi.geektechsol.com�BASE_URLc                   �>  � e Zd Zd4dededdfd�Zed� �       Zdeddfd�Zd	eddfd
�Zdededdfd�Z	dededdfd�Z
d5d�Zd5d�Zd5d�Zdeddfd�Zd6dedededededededdfd�Zd7dedededefd�Zd8dededededef
d�Zd9d ed!eeeef      d"eeeef      d#ed$ed%eddfd&�Zdeeef   fd'�Zd:d(ed%edeeef   fd)�Zdej6                  fd*�Zededej6                  fd+��       Zededefd,��       Zdefd-�Zed.edefd/��       Z d5d0�Z!dee   fd1�Z"e#d2� �       Z$d3� Z%y);�Messager�client_secret�webhook_url�returnNc                 �<   � || _         || _        d | _        d | _        y �N)r
   r   �opened_chat_id�number)�selfr
   r   s      �api/messager.py�__init__zMessager.__init__   s!   � �"/��� +���-1���%)���    c                 �\   � t        j                  dt        | �      �      }|st        d�      �y )Nz?^\+?(\d{1,3})?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$zInvalid phone number!)�re�match�str�ChildProcessError)r   �matchess     r   �validate_numberzMessager.validate_number   s.   � ��(�(�]�_b�ci�_j�k���#�$;�<�<� r   r   c                 �   � | j                  |�       |j                  d�      j                  dd�      | _        | j                  � d�| _        y )N�+� � z@c.us)r   �removeprefix�replacer   r   )r   r   s     r   �set_receiverzMessager.set_receiver   sB   � ����V�$��)�)�#�.�6�6�s�B�?���!%����U�3��r   �messagec                 �~   � | j                  | j                  �       | j                  d| j                  |d��      �      S )N�sendTextr   )�text�session)r   r   �request�get_payload)r   r#   s     r   �send_messagezMessager.send_message"   s5   � ����T�[�[�)��|�|�J��(8�(8�g�r�(8�(R�S�Sr   �_message_idr&   c                 �^   � dddd�}| j                  |d|� ���      }| j                  d|�      S )Nz
image/jpegz
image.jpeg�#)�mimetype�filename�urlzHere is a picture of a ��file�caption�	sendImage)r)   r(   )r   r+   r&   r2   �payloads        r   �replyzMessager.reply&   s?   � �,8�l�[^�_��"&�"2�"2��H_�`d�_e�Ff�"2�"g���|�|�K��1�1r   �
message_id�participantc                 �H   � | j                  d| j                  ||��      �      S )N�sendSeen)�	messageIdr8   �r(   r)   )r   r7   r8   s      r   �	send_seenzMessager.send_seen+   s$   � ��|�|�J��(8�(8�:�[f�(8�(g�h�hr   c                 �.   � | j                  dddid��      S )Nzsessions/logout�namez	<session>F)�return_value)r(   �r   s    r   �logoutzMessager.logout.   s   � ��|�|�-���/D�SX�|�Y�Yr   c                 �B   � | j                  d| j                  �       �      S )N�startTypingr<   rA   s    r   �start_typingzMessager.start_typing1   s   � ��|�|�M�4�+;�+;�+=�>�>r   c                 �B   � | j                  d| j                  �       �      S )N�
stopTypingr<   rA   s    r   �stop_typingzMessager.stop_typing4   s   � ��|�|�L�$�*:�*:�*<�=�=r   �secondsc                 �n   � | j                  �        t        j                  |�       | j                  �        y r   )rE   �time�sleeprH   )r   rI   s     r   �typingzMessager.typing7   s&   � ������
�
�7�����r   �datar/   �filetyper3   �include_prefix�already_in_base64�	link_pathc                 ��   � | j                  | j                  �       |s| j                  |�      n|}| j                  |�      }	|rd|	� d�nd}
| j	                  |	|� d|� �|
� |� �d�|��      }| j                  ||�      S )Nzdata:z;base64,r   �.)r.   r/   rN   r1   )r   r   �string_to_base64�get_mimetyper)   r(   )r   rN   r/   rO   r3   rP   rQ   rR   �base64_filer.   �prefixr5   s               r   �	send_filezMessager.send_file<   s�   � ����T�[�[�)�>O�4�0�0��6�UY���)�)�(�3��/=�5��
�(�+�2��"&�"2�"2�X�HP�z�QR�S[�R\�E]�DJ�8�K�=�AY�9[�dk� #3� #m�� �|�|�I�w�/�/r   c                 �0   � | j                  ||d|d|��      S )N�pdfF�rQ   �rY   )r   rN   r/   r3   rQ   s        r   �send_pdfzMessager.send_pdfI   s   � ��~�~�d�H�e�W�e�Wh�~�i�ir   c                 �0   � | j                  ||||d|��      S )NTr\   r]   )r   rN   r/   r3   rO   rQ   s         r   �
send_imagezMessager.send_imageL   s   � ��~�~�d�H�h���Yj�~�k�kr   �placer5   �headers�log_requestr@   �kwargsc                 ��  � |�| j                  �       n|}|�| j                  �       n|}|rt        d|� d|� ��       t        t        |�      }	  |t
        � d|� �f||d�|��}	|	j                  �        |r|	j                  �       S y # t        j                  t        j                  j                  t        j                  j                  t        j                  f$ r t        d�      �w xY w)Nz*[GTS-Whatsapp] Sent request with headers: z, And with payload: z/api/)rb   �jsonzFFailed to connect to whatsapp, You might be sending too many requests!)�get_headersr)   �print�getattr�requestsr   �raise_for_status�ConnectionError�urllib3�
exceptions�MaxRetryError�NewConnectionError�socket�gaierrorr   rf   )
r   ra   r5   rb   rc   �request_typer@   rd   �func�responses
             r   r(   zMessager.requestO   s�   � �(/��$�"�"�$�W��(/��$�"�"�$�W����>�w�i�G[�\c�[d�e�f��x��.��	n�*.�(��5���/H�*r�RY�`g�*r�kq�*r�H��%�%�'� ��=�=�?�"� �� �(�(�'�*<�*<�*J�*J�G�L^�L^�Lq�Lq�sy�  tC�  tC�  D� 	n�#�$l�m�m�	n�s   �%B �A!C&c                 �    � | j                   dd�S )N�application/json��ClientSecretzContent-Type)r
   rA   s    r   rg   zMessager.get_headers`   s   � � $� 2� 2�DV�W�Wr   �	chat_infoc                 �b   � |r| j                   | j                  d�ni }|j                  |�       |S )N)�chatIdr'   )r   r
   �update)r   rz   rd   r5   s       r   r)   zMessager.get_payloadc   s.   � �dm�T�-@�-@�T�M_�M_�"`�su�����v���r   c                 �   � | j                  �        | j                  �        | j                  | j                  �       �      S r   )rB   �start_session�text_to_qrcode_image�
get_qrcoderA   s    r   �authenticatezMessager.authenticatei   s/   � ����������(�(����):�;�;r   c                 ��   � t        j                  dt         j                  j                  dd��      }|j	                  | �       |j                  d��       |j                  dd�	�      S )
N�   �
   �   )�version�error_correction�box_size�borderT)�fit�black�white)�fill�
back_color)�qrcode�QRCode�	constants�ERROR_CORRECT_L�add_data�make�
make_image)r&   �qrs     r   r�   zMessager.text_to_qrcode_imagen   sQ   � ��]�]�1�v�7G�7G�7W�7W�bd�mn�o��
���D��
���D����}�}�'�g�}�>�>r   c                 �N   � t        j                  | �      }|j                  d�      S )Nzutf-8)�base64�	b64encode�decode)r&   �text_base64s     r   rU   zMessager.string_to_base64v   s#   � ��&�&�t�,���!�!�'�*�*r   c                 �  � | j                   dd�}t        j                  t        dz   |��      }|j                  dk(  ry	 |j                  �       }|ddik(  rt        d	�      �|j                  d
d�      dk(  S # t        j                  $ r Y yw xY w)Nrw   rx   z/api/sessions/<session>/me)rb   i�  F�errorzInvalid ClientSecretz<Your client secret is invalid. Please make sure its correct.�statusz
LOGGED OUT�WORKING)r
   rj   �getr   �status_coderf   �JSONDecodeErrorr   )r   rb   r(   �infos       r   �is_logged_inzMessager.is_logged_in{   s�   � �#'�#5�#5�GY�Z���,�,�x�,F�G�QX�Y�����#�%��	��<�<�>�D� �G�3�4�4�#�$b�c�c��x�x��,�/�9�<�<�� �'�'� 	��	�s   �A6 �6B�B�	extensionc                 �8   � t        j                  d| � ��      d   S )Nzfile.r   )�	mimetypes�
guess_type)r�   s    r   rV   zMessager.get_mimetype�   s   � ��#�#�e�I�;�$7�8��;�;r   c           	      �l   � dddddd�i| j                   ddgdddd	�gdd
�d�}| j                  d|�       y)z�
        Starts a whatsapp session. Each device can have a session. Session's
        initially don't have any information, But scanning a qr code will set up the session and
        insert passwords, keys, etc
        r   N�storeTF)�enabled�fullSyncr#   zsession.status)r0   �events�hmac�retries�customHeaders)�proxy�noweb�webhooks�debug)r?   �configzsessions/start)r   r(   )r   r5   s     r   r   zMessager.start_session�   sj   � � ���#'�$)���  $�/�/�%�,�#� !%�#'�)-�	�� �)�#
��4 	���%�w�/r   c                 �  � 	 t        j                  t        � d�| j                  �       ��      }|j	                  �       }dt        |j                  �       �      v r|d   dk(  rt        j                  d�       �v|j                  dk7  r)t        d|j                  � d|j	                  �       � ��      �|j	                  �       j                  d	�      S )
Nz!/api/<session>/auth/qr?format=raw)r0   rb   r�   zUnprocessable Entity�   ��   z&Failed to fetch QR Code. Status code: z, Response: 
�value)rj   r�   r   rg   rf   �list�keysrK   rL   r�   r   )r   ru   �results      r   r�   zMessager.get_qrcode�   s�   � ��*2�,�,��j� A�B��(�(�*�+�H�
 &.�]�]�_�F��$�v�{�{�}�-�-�&��/�E[�2[��
�
�1����#�#�s�*�'�*P�QY�Qe�Qe�Pf�ft�u}�  vC�  vC�  vE�  uF�  )G�  H�  H��=�=�?�&�&�w�/�/r   c                 �d   � | j                  d| j                  �       | j                  �       d��      S )N�usager�   )r5   rb   rs   )r(   r)   rg   rA   s    r   �requests_infozMessager.requests_info�   s,   � ��|�|�G�T�-=�-=�-?��IY�IY�I[�jo�|�p�pr   c                 �D   � | j                  d| j                  � �i d��      S )Nzcontacts/all?session=r�   )r5   rs   )r(   r
   rA   s    r   �get_contactszMessager.get_contacts�   s(   � ��|�|�3�D�4F�4F�3G�H�RT�ch�|�i�ir   )z9https://webhook.site/2778607e-15e4-4af3-95a2-ee91f371be8e)r   N)�image�jpgr   TF�sendFile)�documentr   F)r�   r   r�   F)NNF�postT)T)&�__name__�
__module__�__qualname__r   r   �staticmethodr   r"   r*   r6   r=   rB   rE   rH   �intrM   �bytes�boolrY   r^   r`   r   r   r   r(   rg   r)   r   r�   r�   rU   r�   rV   r   r�   �propertyr�   r�   � r   r   r	   r	      s�  � �*�c� *�� *�  C� *� �=� �=�
4�3� 4�4� 4�
T�C� T�D� T�2�� 2�C� 2�D� 2�
i�C� i�c� i�d� i�Z�?�>��c� �d� �
0�e� 0�s� 0�� 0�^a� 0�x|� 0�  Y]� 0�  ru� 0�  GK� 0�j�U� j�c� j�� j�fj� j�l�u� l�� l�� l�\_� l�  }A� l�#�S� #�8�D��c��N�+C� #�U]�^b�cf�hk�ck�^l�Um� #�  DH� #�  uy� #�  LO� #�  TX� #�"X�T�#�s�(�^� X��T� �C� �D��c��N� �<�e�k�k� <�
 �?�3� ?�5�;�;� ?� �?� �+�u� +�� +� �+�=�d� =�" �<�� <�� <� �<� 0�D0�H�S�M� 0�$ �q� �q�jr   r	   )rM   r   r   r   �PILr   rj   rK   r�   r�   r�   r   rq   rm   r   r   �__annotations__r	   r�   r   r   �<module>r�      s@   �� &� &� � � � � � � 	� � � 2��#� 1�yj� yjr   