�
    ώ(g�  �                   �4   � d dl Z  G d� d�      Z G d� d�      Zy)�    Nc            	       �d   � e Zd Z	 	 	 ddedededefd�Zdeeef   defd�Zdefd	�Z	de
e   fd
�Zy)�TextTemplate�template_string�	seperator�allow_invalid_names�allow_nonexistent_namesc                 �<   � || _         || _        || _        || _        y)z�
        Format for template strings:
            'Hello, $name! I heard you're feeling $mood'

        Although the delimiter (seperator) can be changed
        N)r   �	separatorr   r   )�selfr   r   r   r   s        �wizard/zstring/classes.py�__init__zTextTemplate.__init__   s#   � � %4���'���)<�� �-D��$�    �	variables�returnc                 �,  � | j                   }|j                  �       D ]t  \  }}| j                  s|j                  �       st	        d|� d��      �| j
                  j                  d|�      }|}|j                  ||�      }||k(  s�gt	        d|� d��      � |S )NzThe variable name zM is not a proper variable name. To disable this, Set allow_invalid_names=True�valuezThe variable name 'zh' doesnt exist in the template with a valid format. Disable this by setting allow_nonexistent_names=True)r   �itemsr   �isidentifier�
ValueErrorr
   �replace)r   r   �result�namer   �value_replacer�previous_results          r   �fillzTextTemplate.fill   s�   � ��%�%��$�?�?�,� 	g�K�D�%��+�+�D�4E�4E�4G� �#5�d�V�  <I�  "J�  K�  K� "�^�^�3�3�G�T�B�N�$�O��^�^�N�E�:�F� �&�(� �#6�t�f�  =e�  "f�  g�  g�	g�  �r   c                 �   � t        j                  | j                  �      j                  dd�      }t	        t        j
                  || j                  �      �      S )zn
        Counts the number of variables in the template string
        based on the separator format.
        r   z\w+)�re�escaper
   r   �len�findallr   �r   �patterns     r   �count_variableszTextTemplate.count_variables+   s?   � �
 �)�)�D�N�N�+�3�3�G�V�D���2�:�:�g�t�';�';�<�=�=r   c                 �   � t        j                  | j                  �      j                  dd�      }t        j                  || j
                  �      S )zo
        Gets the list of variable names in the template string
        based on the separator format.
        r   z(\w+))r   r   r
   r   r    r   r!   s     r   �get_variableszTextTemplate.get_variables3   s:   � �
 �)�)�D�N�N�+�3�3�G�X�F���z�z�'�4�#7�#7�8�8r   N)z$valueFF)�__name__�
__module__�__qualname__�str�boolr   �dictr   �intr#   �listr%   � r   r   r   r      sr   � � #+�-2�16�	E�"%�E��E� '+�E� +/�	E�"�d�3��8�n� �� �*>�� >�9�t�C�y� 9r   r   c                   �>   � e Zd Zdededefd�Zdedeeef   defd�Zy)	�StringFormatterr   �format_moder   c                 �   � t        d�      �)NzRStringFormatter shouldn't be used directly. Instead, You should create a subclass.)�NotImplementedError)r   r   r1   s      r   �formatzStringFormatter.format=   s   � �!�"v�w�wr   �text�valuesc                 �  � t        j                  d|�      }|}|D ]�  }|j                  d�      }|d   }t        |�      dk\  r|d   j	                  d�      nd}|j                  |d|z   d	z   �      }	d
| j                  j                  j                  v r| j                  |	|�      }
n| j                  |	�      }
|j                  d|� d	�|
�      }�� |S )Nz\{(.*?)}�:r   �   �   � � �{�}r1   )
r   r    �splitr   �removeprefix�getr4   �__code__�co_varnamesr   )r   r5   r6   �placeholders�new_text�placeholder�splitted�key�format_specr   �formatted_values              r   �format_stringzStringFormatter.format_string@   s�   � ��z�z�+�t�4����'� 	O�K�"�(�(��-�H��1�+�C�;>�x�=�A�;M�(�1�+�2�2�3�7�SU�K��J�J�s�C�#�I��O�4�E����� 4� 4� @� @�@�"&�+�+�e�[�"A��"&�+�+�e�"4���'�'�"�[�M��(<�o�N�H�	O� �r   N)r&   r'   r(   r)   r4   r+   rK   r.   r   r   r0   r0   <   sB   � �x�C� x�c� x�c� x��#� �t�C��H�~� �#� r   r0   )r   r   r0   r.   r   r   �<module>rL      s   �� 	�59� 59�p� r   