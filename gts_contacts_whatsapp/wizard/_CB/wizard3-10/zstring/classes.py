o
    ̎(g�  �                   @   s(   d dl Z G dd� d�ZG dd� d�ZdS )�    Nc                	   @   sh   e Zd Z			ddedededefdd�Zd	eeef d
efdd�Zd
efdd�Z	d
e
e fdd�ZdS )�TextTemplate�$valueF�template_string�	seperator�allow_invalid_names�allow_nonexistent_namesc                 C   s   || _ || _|| _|| _dS )z�
        Format for template strings:
            'Hello, $name! I heard you're feeling $mood'

        Although the delimiter (seperator) can be changed
        N)r   �	separatorr   r   )�selfr   r   r   r   � r
   �wizard/zstring/classes.py�__init__   s   
zTextTemplate.__init__�	variables�returnc                 C   sp   | j }|�� D ].\}}| js|�� std|� d���| j�d|�}|}|�||�}||kr5td|� d���q|S )NzThe variable name zM is not a proper variable name. To disable this, Set allow_invalid_names=True�valuezThe variable name 'zh' doesnt exist in the template with a valid format. Disable this by setting allow_nonexistent_names=True)r   �itemsr   �isidentifier�
ValueErrorr   �replace)r	   r   �result�namer   Zvalue_replacerZprevious_resultr
   r
   r   �fill   s   �zTextTemplate.fillc                 C   s&   t �| j��dd�}tt �|| j��S )zn
        Counts the number of variables in the template string
        based on the separator format.
        r   z\w+)�re�escaper   r   �len�findallr   �r	   �patternr
   r
   r   �count_variables+   s   zTextTemplate.count_variablesc                 C   s"   t �| j��dd�}t �|| j�S )zo
        Gets the list of variable names in the template string
        based on the separator format.
        r   z(\w+))r   r   r   r   r   r   r   r
   r
   r   �get_variables3   s   zTextTemplate.get_variablesN)r   FF)�__name__�
__module__�__qualname__�str�boolr   �dictr   �intr   �listr   r
   r
   r
   r   r      s     ����
�r   c                   @   s@   e Zd Zdededefdd�Zdedeeef defdd	�Zd
S )�StringFormatterr   �format_moder   c                 C   s   t d��)NzRStringFormatter shouldn't be used directly. Instead, You should create a subclass.)�NotImplementedError)r	   r   r(   r
   r
   r   �format=   s   zStringFormatter.format�text�valuesc                 C   s�   t �d|�}|}|D ]A}|�d�}|d }t|�dkr"|d �d�nd}|�|d| d	 �}	d
| jjjv r<| �|	|�}
n| �|	�}
|�	d|� d	�|
�}q
|S )Nz\{(.*?)}�:r   �   �   � � �{�}r(   )
r   r   �splitr   �removeprefix�getr*   �__code__�co_varnamesr   )r	   r+   r,   ZplaceholdersZnew_textZplaceholderZsplitted�key�format_specr   Zformatted_valuer
   r
   r   �format_string@   s   

zStringFormatter.format_stringN)r   r    r!   r"   r*   r$   r;   r
   r
   r
   r   r'   <   s    "r'   )r   r   r'   r
   r
   r
   r   �<module>   s    8