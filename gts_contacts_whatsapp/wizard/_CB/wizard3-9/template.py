a
    ʎ(g�  �                   @   s2   d dl mZ ddlmZ g d�ZG dd� d�ZdS )�   )�zstring�   )�Config))Zsales_quotationszSales Quotation/Order)Zpurchase_quotationzPurchase Quotation)ZinvoiceZInvoicec                   @   sR   e Zd Zeeeef d�dd�Zee d�dd�Ze	ee ee d�dd	��Z
d
S )�Template)�template_text�pathsc                 C   s   || _ t�|�| _|| _d S �N)r   r   ZTextTemplate�templater   )�selfr   r   � r   �wizard/template.py�__init__   s    zTemplate.__init__)�objectsc                 C   sP   | j �� }i }|D ]0}| j�|�}|s(q| �||�d��}|||< q| j �|�S )N�.)r	   Zget_variablesr   �get�split�fill)r
   r   �	variables�results�var�path�resultr   r   r   r      s    

zTemplate.fill)r   �namesc              
   C   sL   | D ]B}z"|}|D ]}t ||�}q|W   S  ttfyD   Y qY q0 qd S r   )�getattr�AttributeError�	NameError)r   r   �object�current�namer   r   r   r       s    
zTemplate.getN)�__name__�
__module__�__qualname__�str�dictr   �listr   r   �staticmethodr   r   r   r   r   r      s   r   N)� r   Z	global_pyr   ZTEMPLATES_SELECTIONr   r   r   r   r   �<module>   s   