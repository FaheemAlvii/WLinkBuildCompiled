o
    ˎ(g�  �                   @   s6   d dl mZ ddlmZmZmZ G dd� dej�ZdS )�   )�Config�    )�api�fields�modelsc                   @   s>   e Zd ZdZejdddd� d�Ze�d�dd	� �Z	d
d� Z
dS )�BaseURLEditor�gts_whatsapp.base_url_editorzBase URLTc                 C   s   t | ��d�S )N�base_url)r   �get��self� r   �wizard/base_url_editor.py�<lambda>   s    zBaseURLEditor.<lambda>)�stringZrequired�defaultr	   c                 C   s8   | j r| j �d�r| j �d� t| ��d| j � d S d S )N�/r	   )r	   �endswith�removesuffixr   �setr   r   r   r   �onchange_base_url
   s
   �zBaseURLEditor.onchange_base_urlc                 C   s4   t | ��dd� t | ��d�| _ddddd| jd�S )	Nr	   zhttps://whatapi.geektechsol.comzir.actions.act_windowzWhatsapp Base URL EditorZformr   �new)�type�nameZ	view_modeZ	res_model�targetZres_id)r   r   r
   r	   �idr   r   r   r   �reset   s   �zBaseURLEditor.resetN)�__name__�
__module__�__qualname__�_namer   ZCharr	   r   Zonchanger   r   r   r   r   r   r      s    
r   N)Z	global_pyr   Zodoor   r   r   ZModelr   r   r   r   r   �<module>   s    