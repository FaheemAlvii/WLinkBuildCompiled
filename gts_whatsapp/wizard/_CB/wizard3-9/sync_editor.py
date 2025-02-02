a
    ʎ(g�  �                   @   s\   d dl mZmZmZ d dlmZ ddlmZmZm	Z	 G dd� dej
�ZG dd� dej�Zd	S )
�    )�api�fields�models)�ValidationError�   )�get_default_connection�	get_phone�
get_reopenc                   @   sN   e Zd ZdZdZejddd�Zejddd�Zejddd�Z	ej
ddd	d
�ZdS )�Contact�gts_whatsapp.contactz Contact for gts_whatsapp.contactZPhoneT��string�required�NameZUsernameZKeepF)r   r   �defaultN)�__name__�
__module__�__qualname__�_name�_descriptionr   ZChar�phone�name�usernameZBoolean�keep� r   r   �wizard/sync_editor.pyr
      s   r
   c                   @   s�   e Zd ZdZdZejdeddd�Zej	dddd	�Z
eeeeef  d
�dd�Ze�d�dd� �Zdd� Zdeed�dd�Zdd� Zdd� Zdd� ZdS )�
SyncEditorzgts_whatsapp.sync_editorz'SyncEditor for gts_whatsapp.sync_editorzwhatsapp.connectionzWhatsapp ConnectionT)r   r   r   r   zContacts to syncr   )�datac                 C   s�   g }g }t |�D ]F\}\}}}d}|}	|dkrBd}t|�d | }	|�|	||||f� q|jdd� d� |D ]4\}
}}}}| jd �||||d	��}|�|j� qld
d|fg| _d S )NT�*Invalid name*F�   c                 S   s   | d S )Nr   r   )�xr   r   r   �<lambda>'   �    z+SyncEditor.setup_contacts.<locals>.<lambda>)�keyr   )r   r   r   r   �   r   )�	enumerate�len�append�sort�env�create�id�contacts_to_sync)�selfr   Zcontact_idsZsorted_data�indexr   r   r   r   Zsorter�_�contactr   r   r   �setup_contacts   s    zSyncEditor.setup_contacts�
connectionc                 C   st   | j rp| j �t�}g }|D ]J}t|d �}|�dd�}|�dd�}|dkrT|dkrTq|�|||f� q| �|� d S )Nr+   r   z*Invalid username*Zpushnamer   )r2   Zget_contactsr   r   �getr'   r1   )r-   Zcontactsr   r0   r   r   r   r   r   r   �reload_data0   s    zSyncEditor.reload_datac                 C   s2   | j D ]&}|jr| jd �|j|jdd�� qd S )Nzres.partnerF)r   r   Z
is_company)r,   r   r)   r*   r   r   )r-   r0   r   r   r   �synchronizeC   s    
zSyncEditor.synchronizeF)r   �reloadc                 C   s4   | j D ]}t|t� t� �|_q|r*| ��  t| d�S )NzWhatsapp Synchronization)r,   �eval�globals�localsr   r4   r	   )r-   r   r6   �recordr   r   r   �base_selectI   s    
zSyncEditor.base_selectc                 C   s
   | � d�S )N�True�r;   �r-   r   r   r   �
select_allQ   r"   zSyncEditor.select_allc                 C   s
   | � d�S )N�Falser=   r>   r   r   r   �deselect_allR   r"   zSyncEditor.deselect_allc                 C   s
   | � d�S )Nzrecord.name == "*Invalid name*"r=   r>   r   r   r   �select_saved_contactsS   r"   z SyncEditor.select_saved_contactsN)F)r   r   r   r   r   r   ZMany2oner   r2   Z	Many2manyr,   �list�tuple�strr1   r   Zonchanger4   r5   �boolr;   r?   rA   rB   r   r   r   r   r      s   
r   N)Zodoor   r   r   Zodoo.exceptionsr   Z	global_pyr   r   r	   ZTransientModelr
   ZModelr   r   r   r   r   �<module>   s   
