# Ecommerce Store - Full Website
## PPM 2nd Project

Questo è un progetto e-commerce sviluppato in Django. Gli utenti possono registrarsi, effettuare ordini, scrivere recensioni, e gestire il proprio account (compreso cambio password). Gli amministratori possono gestire lo stato degli ordini.

## Funzionalità principali

- Registrazione e autenticazione utenti
- Visualizzazione prodotti per categoria
- Carrello e checkout
- Cronologia ordini
- Recensioni con valutazione da 1 a 5 stelle
- Cambio password
- Dashboard admin con controllo ordini
- Interfaccia responsive con Bootstrap

---

## Tech stack

- **Backend**: Django 4.2
- **Database**: SQLite
- **Frontend**: HTML, Bootstrap 5
- **Autenticazione**: built-in Django Auth

---

## Installazione

1. **Clona il repository**

```bash
git clone https://github.com/petrucciandrea/fw_ecommerce.git
cd fw_ecommerce
```

2. **Crea un ambiente virtuale**

```bash
python -m venv venv
source venv/bin/activate  # su Windows: venv\Scripts\activate
```

3. **Installa le dipendenze**

```bash
pip install -r requirements.txt
```

4. **Applica le migrazioni**

```bash
python manage.py migrate
```

5. **Avvia il server**

```bash
python manage.py runserver
```

Ora puoi visitare http://127.0.0.1:8000 nel tuo browser.**

## Struttura del progetto

```bash
csharp
Copy
Edit
fw_ecommerce/
├── account/                 # Gestione utente
├── shop/                    # Gestione shop
├── templates/
│   ├── registration/        # Account
│   └── shop/                # Home, ordini, details
├── static/                  # File statici (JS, CSS, immagini)
├── manage.py
└── requirements.txt
```

## Account default

Amministratore
- **Username:** admin
- **Password:** Universita

Utente 1
- **Username:** mrossi
- **Password:** ProvaProva

Utente 2
- **Username:** ppallino
- **Password:** ProvaProva