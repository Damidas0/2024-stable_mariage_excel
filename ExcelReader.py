import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename


# Fonction pour charger le fichier Excel
def load_excel_file():
    """Ouvre boite de dialogue et charge l'excel séléctionné

    Returns:
        ExcelFile: fichier Excel séléctionné
    """
    Tk().withdraw()  # Masque la fenêtre principale de Tkinter
    file_path = askopenfilename(title="Sélectionnez le fichier Excel")
    return pd.ExcelFile(file_path)

# Fonction pour lire les données des participants
def read_participant_data(excel_file):
    """Lis les inscriptions dans l'Excel

    Args:
        excel_file (ExcelFile): fichier excel à lire

    Returns:
        DataFrame:
    """
    participants = pd.read_excel(excel_file, sheet_name='Inscrits')
    return participants #pd.read_excel(excel_file, sheet_name='Inscrits')

def read_workshop_data(excel_file):
    """Lis les inscriptions dans l'Excel 

    Args:
        excel_file (ExcelFile): fichier excel à lire

    Returns:
        DataFrame: 
    """
    ateliers = pd.read_excel(excel_file, sheet_name='Ateliers')
    
    return ateliers #pd.read_excel(excel_file, sheet_name='Ateliers')

def delete_attribution(excel_file):
    excel_file.sheet['Attribution'].delete() 
    

# Fonction pour enregistrer les attributions dans une nouvelle feuille Excel
def save_assignments(excel_file, assignments):
    writer = pd.ExcelWriter(excel_file, engine='openpyxl', mode='a')
    
    writer.remove_sheet(writer['Attributions'])
    
    assignment_data = []
    for email, assigned_workshops in assignments.items():
        assignment_data.append({'Email': email, 'Ateliers Attribués': ', '.join(assigned_workshops)})
    df = pd.DataFrame(assignment_data)
    
    df.to_excel(writer, sheet_name='Attributions', index=False)
    writer.close()