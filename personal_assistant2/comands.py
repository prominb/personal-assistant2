from personal_assistant2.colors import * 
PISKAZKA_SHOW_ALL = f"\nКоманда - {GREEN}show all{YLLOW} - покаже доступні контакти{DEFALUT}"

LIST_COMANDS_BOT = ["hello", "add", "phone", "email", "show all", "change", 'search', 
                    "good bye", "close", "exit", 'sorted', 'notes']
# LIST_COMANDS_BOT = ["hello", "add", "change", "phone", "email", "show all", 'search', "good bye", "close", "exit",
#                     'sorted', 'notes']
DOSTUPNI_COMANDY = f"{RED}Доступні наступні команди : {GREEN}{LIST_COMANDS_BOT}{DEFALUT}"
BAD_COMMAND_ADD = f"{YLLOW}Невірні параметри для команди {GREEN}add{YLLOW} !!!.\n\
                        {RED}# Приклад {GREEN}add{BIRUZA} Імя_контакту{YLLOW} Номер_телефону|Еmail {DEFALUT}"
    
BAD_COMMAND_CHANGE = f"{YLLOW}Невірні параметри для команди {GREEN}change{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}change{BIRUZA} Імя_контакту {GREEN}name {BIRUZA} Нове ім'я "
    
BAD_COMMAND_PHONE = f"{YLLOW}Невірні параметри для команди {GREEN}phone{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}phone{BIRUZA} Імя_контакту{YLLOW} "
    
BAD_COMMAND_SEARCH = f"{YLLOW}Невірні параметри для команди {GREEN}search{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}search{BIRUZA} Імя_контакту{YLLOW} "

BAD_COMMAND_SORTED = f"{YLLOW}Невірні параметри для команди {GREEN}sorted{YLLOW} !!!.\n\
                        {RED}# Приклад {GREEN}sorted{BIRUZA} Шлях_до_папки{YLLOW}"

BAD_COMMAND_NOTES = f"{YLLOW}Невірні параметри для команди {GREEN}notes{YLLOW} !!!.\n\
                        {RED}# Приклад {GREEN}notes{BIRUZA}"

BAD_COMMAND_BIRTHDAYS = f"{YLLOW}Невірні параметри для команди {GREEN}phone{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}phone{BIRUZA} Імя_контакту{YLLOW} "
