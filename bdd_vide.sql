#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------

#------------------------------------------------------------
# Database: careplan
#------------------------------------------------------------

CREATE DATABASE careplan COLLATE utf8_general_ci;
USE careplan;


#------------------------------------------------------------
# Table: Patient
#------------------------------------------------------------

CREATE TABLE Patient(
        ref_patient Int  Auto_increment  NOT NULL ,
        nom         Varchar (50) NOT NULL ,
        prenom      Varchar (50) NOT NULL ,
        num_tel     Char (10) ,
        civilite    Int NOT NULL
	,CONSTRAINT Patient_PK PRIMARY KEY (ref_patient)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: medecin
#------------------------------------------------------------

CREATE TABLE medecin(
        ref_medecin       Int  Auto_increment  NOT NULL ,
        nom               Varchar (50) NOT NULL ,
        prenom            Varchar (50) NOT NULL ,
        num_tel           Char (10) NOT NULL ,
        specialite        Varchar (50) NOT NULL ,
        horaires_lundi    Varchar (50) NOT NULL ,
        horaires_mardi    Varchar (50) NOT NULL ,
        horaires_mercredi Varchar (50) NOT NULL ,
        horaires_jeudi    Varchar (50) NOT NULL ,
        horaires_vendredi Varchar (50) NOT NULL ,
        horaires_samedi   Varchar (50) NOT NULL ,
        horaires_dimanche Varchar (50) NOT NULL
	,CONSTRAINT medecin_PK PRIMARY KEY (ref_medecin)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: horaires_speciaux
#------------------------------------------------------------

CREATE TABLE horaires_speciaux(
        ref_hor_spe       Int  Auto_increment  NOT NULL ,
        date_debut        Date NOT NULL ,
        date_fin          Date NOT NULL ,
        horaires_lundi    Varchar (50) NOT NULL ,
        horaires_mardi    Varchar (50) NOT NULL ,
        horaires_mercredi Varchar (50) NOT NULL ,
        horaires_jeudi    Varchar (50) NOT NULL ,
        horaires_vendredi Varchar (50) NOT NULL ,
        horaires_samedi   Varchar (50) NOT NULL ,
        horaires_dimanche Varchar (50) NOT NULL ,
        ref_medecin       Int NOT NULL
	,CONSTRAINT horaires_speciaux_PK PRIMARY KEY (ref_hor_spe)

	,CONSTRAINT horaires_speciaux_medecin_FK FOREIGN KEY (ref_medecin) REFERENCES medecin(ref_medecin) ON DELETE CASCADE
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: RDV
#------------------------------------------------------------

CREATE TABLE RDV(
        ref_rdv          Int  Auto_increment  NOT NULL ,
        date_heure_debut Datetime NOT NULL ,
        duree            Time NOT NULL ,
        ref_patient      Int NOT NULL ,
        ref_medecin      Int NOT NULL
	,CONSTRAINT RDV_PK PRIMARY KEY (ref_rdv)

	,CONSTRAINT RDV_Patient_FK FOREIGN KEY (ref_patient) REFERENCES Patient(ref_patient) ON DELETE CASCADE
	,CONSTRAINT RDV_medecin_FK FOREIGN KEY (ref_medecin) REFERENCES medecin(ref_medecin) ON DELETE CASCADE
)ENGINE=InnoDB;
