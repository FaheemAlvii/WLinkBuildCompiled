o
    ̎(g�  �                   @   s2   d dl mZ ddlmZ g d�ZG dd� d�ZdS )�   )�zstring�   )�Config))Zsales_quotationszSales Quotation/Order)Zpurchase_quotationzPurchase Quotation)ZinvoiceZInvoicec                   @   sV   e Zd Zdedeeef fdd�Zdee fdd�Ze	dee dee fd	d
��Z
dS )�Template�template_text�pathsc                 C   s   || _ t�|�| _|| _d S �N)r   r   ZTextTemplate�templater   )�selfr   r   � r   �wizard/template.py�__init__   s   
zTemplate.__init__�objectsc                 C   sP   | j �� }i }|D ]}| j�|�}|sq	| �||�d��}|||< q	| j �|�S )N�.)r	   Zget_variablesr   �get�split�fill)r
   r   �	variables�results�var�path�resultr   r   r   r      s   

zTemplate.fill�namesc              
   C   sF   | D ]}z|}|D ]}t ||�}q	|W   S  ttfy    Y qw d S r   )�getattr�AttributeError�	NameError)r   r   �objectZcurrent�namer   r   r   r       s   
��zTemplate.getN)�__name__�
__module__�__qualname__�str�dictr   �listr   r   �staticmethodr   r   r   r   r   r      s
     r   N)� r   Z	global_pyr   ZTEMPLATES_SELECTIONr   r   r   r   r   �<module>   s    