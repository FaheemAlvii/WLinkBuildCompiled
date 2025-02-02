o
    ̎(gG  �                   @   s:   d dl mZmZ ddlmZmZmZ G dd� dej�ZdS )�   )�Config�
get_reopen�    )�api�fields�modelsc                   @   sb   e Zd ZdZdd� Zejedddd�Zejdd	�Z	e
�d
�dd� �Ze
�d�dd� �Zdd� ZdS )�TemplatesEditorzgts_whatsapp.templates_editorc                    s(   dd� � � fdd�t | ��d��� D �S )Nc                 S   s   | � dd�� dd��� S )Nzstock.action_report_� �_� )�replace�
capitalize)�template_id� r   �wizard/templates_editor.py�<lambda>	   �    z8TemplatesEditor.get_template_selection.<locals>.<lambda>c                    s   g | ]}|� |�f�qS r   r   )�.0r   �Zhumanifyr   r   �
<listcomp>
   r   z:TemplatesEditor.get_template_selection.<locals>.<listcomp>�templates_text)r   �get�keys��selfr   r   r   �get_template_selection   s    z&TemplatesEditor.get_template_selectionzTemplate NameTZsales_quotations)�stringZrequired�defaultzTemplate Text)r   �templatec                 C   s    | j rt| ��| j �| _d S d S �N)r   r   �get_template_text�template_textr   r   r   r   �onchange_template   s   �z!TemplatesEditor.onchange_templater!   c                 C   s"   | j rt| ��| j| j � d S d S r   )r!   r   Zset_template_textr   r   r   r   r   �onchange_template_text   s   �z&TemplatesEditor.onchange_template_textc                 C   s4   t | ��dd � t | � t | ��| j�| _t| d�S )Nr   zWhatsapp Templates Editor)r   �setr    r   r!   r   r   r   r   r   �reset   s   
zTemplatesEditor.resetN)�__name__�
__module__�__qualname__�_namer   r   Z	Selectionr   ZTextr!   r   Zonchanger"   r#   r%   r   r   r   r   r      s    

r   N)	Z	global_pyr   r   Zodoor   r   r   ZTransientModelr   r   r   r   r   �<module>   s    