#!/usr/bin/env python3
import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.prompt import Prompt, Confirm
from rich import box
import pyfiglet

from crypto.encryptor import FileEncryptor
from crypto.decryptor import FileDecryptor
from utils.file_handler import FileHandler
from utils.validator import Validator

console = Console()
file_handler = FileHandler()
validator = Validator()


def banner():
    """Display awesome banner"""
    banner_text = pyfiglet.figlet_format("FILE ENCRYPTOR", font="slant")
    console.print(Panel(
        banner_text,
        title="[bold red]🔐 FILE ENCRYPTOR/DECRYPTOR[/bold red]",
        subtitle="[bold yellow]Secure Your Files with AES-256[/bold yellow]",
        border_style="cyan",
        padding=(1, 2)
    ))

def warning():
    """Security warning"""
    warning_panel = Panel(
        "[bold red]⚠️  SECURITY WARNING[/bold red]\n"
        "• Keep your passwords safe and secure\n"
        "• Never share encrypted files without passwords\n"
        "• Backup your files before encryption\n"
        "• Dev: Cibenk/Wh04ami",
        title="IMPORTANT",
        border_style="red",
        box=box.DOUBLE
    )
    console.print(warning_panel)

def main_menu():
    """Display main menu"""
    table = Table(title="🚀 MAIN MENU", show_header=True, header_style="bold magenta")
    table.add_column("No", style="cyan", width=5)
    table.add_column("Module", style="white")
    table.add_column("Description", style="green")
    
    table.add_row("1", "🔒 Encrypt File", "Encrypt files with password")
    table.add_row("2", "🔓 Decrypt File", "Decrypt encrypted files")
    table.add_row("3", "📁 Batch Encrypt", "Encrypt multiple files")
    table.add_row("4", "🛡️ Password Tools", "Password utilities")
    table.add_row("5", "ℹ️ File Info", "Get file information")
    table.add_row("0", "🚪 Exit", "Exit application")
    
    console.print(table)

def encrypt_file_menu():
    """Encrypt single file"""
    console.print("\n[bold cyan]🔒 ENCRYPT FILE[/bold cyan]")
    
    file_path = Prompt.ask("[+] Enter file path to encrypt")
    
    if not validator.file_exists(file_path):
        console.print("[red]❌ File not found![/red]")
        return
    
    if not validator.is_readable(file_path):
        console.print("[red]❌ Cannot read file![/red]")
        return
    
    # Show file info
    file_info = file_handler.get_file_info(file_path)
    console.print(f"[yellow]📄 File: {file_info['name']}[/yellow]")
    console.print(f"[blue]📊 Size: {file_info['size']} MB[/blue]")
    console.print(f"[green]📝 Type: {file_info['type']}[/green]")
    
    password = Prompt.ask("[+] Enter encryption password", password=True)
    confirm_password = Prompt.ask("[+] Confirm password", password=True)
    
    if password != confirm_password:
        console.print("[red]❌ Passwords don't match![/red]")
        return
    
    if not validator.is_strong_password(password):
        console.print("[yellow]⚠️  Weak password! Recommend using 8+ characters with mix of letters, numbers and symbols[/yellow]")
        if not Confirm.ask("[yellow]Continue with weak password?[/yellow]"):
            return
    
    # Encrypt file
    encryptor = FileEncryptor()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        task = progress.add_task("[cyan]Encrypting file...", total=100)
        
        try:
            output_path = encryptor.encrypt_file(file_path, password)
            
            for i in range(10):
                progress.update(task, advance=10)
            
            console.print(f"[green]✅ File encrypted successfully![/green]")
            console.print(f"[blue]📁 Output: {output_path}[/blue]")
            
            # Show encryption details
            encrypted_info = file_handler.get_file_info(output_path)
            console.print(f"[yellow]🔐 Encrypted size: {encrypted_info['size']} MB[/yellow]")
            
        except Exception as e:
            console.print(f"[red]❌ Encryption failed: {str(e)}[/red]")

def decrypt_file_menu():
    """Decrypt single file"""
    console.print("\n[bold cyan]🔓 DECRYPT FILE[/bold cyan]")
    
    file_path = Prompt.ask("[+] Enter encrypted file path")
    
    if not validator.file_exists(file_path):
        console.print("[red]❌ File not found![/red]")
        return
    
    if not file_path.endswith('.encrypted'):
        console.print("[yellow]⚠️  File doesn't have .encrypted extension[/yellow]")
        if not Confirm.ask("[yellow]Continue anyway?[/yellow]"):
            return
    
    password = Prompt.ask("[+] Enter decryption password", password=True)
    
    # Decrypt file
    decryptor = FileDecryptor()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        task = progress.add_task("[cyan]Decrypting file...", total=100)
        
        try:
            output_path = decryptor.decrypt_file(file_path, password)
            
            for i in range(10):
                progress.update(task, advance=10)
            
            console.print(f"[green]✅ File decrypted successfully![/green]")
            console.print(f"[blue]📁 Output: {output_path}[/blue]")
            
        except Exception as e:
            console.print(f"[red]❌ Decryption failed: {str(e)}[/red]")
            console.print("[yellow]⚠️  Wrong password or corrupted file[/yellow]")

def batch_encrypt_menu():
    """Encrypt multiple files"""
    console.print("\n[bold cyan]📁 BATCH ENCRYPTION[/bold cyan]")
    
    folder_path = Prompt.ask("[+] Enter folder path")
    
    if not validator.folder_exists(folder_path):
        console.print("[red]❌ Folder not found![/red]")
        return
    
    # Get files in folder
    files = file_handler.get_files_in_folder(folder_path)
    if not files:
        console.print("[red]❌ No files found in folder![/red]")
        return
    
    console.print(f"[green]📂 Found {len(files)} files[/green]")
    
    # Show file list
    file_table = Table(title="Files to Encrypt", show_header=True)
    file_table.add_column("No", style="cyan")
    file_table.add_column("File", style="white")
    file_table.add_column("Size", style="yellow")
    
    for i, file_path in enumerate(files[:10], 1):  # Show first 10 files
        info = file_handler.get_file_info(file_path)
        file_table.add_row(str(i), info['name'], f"{info['size']} MB")
    
    if len(files) > 10:
        file_table.add_row("...", f"... and {len(files) - 10} more", "...")
    
    console.print(file_table)
    
    password = Prompt.ask("[+] Enter encryption password", password=True)
    
    if not Confirm.ask(f"[yellow]Encrypt {len(files)} files?[/yellow]"):
        return
    
    encryptor = FileEncryptor()
    success_count = 0
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        task = progress.add_task("[cyan]Encrypting files...", total=len(files))
        
        for file_path in files:
            try:
                encryptor.encrypt_file(file_path, password)
                success_count += 1
            except Exception as e:
                console.print(f"[red]❌ Failed to encrypt {os.path.basename(file_path)}: {str(e)}[/red]")
            
            progress.update(task, advance=1)
    
    console.print(f"[green]✅ Successfully encrypted {success_count}/{len(files)} files[/green]")

def password_tools_menu():
    """Password utilities"""
    console.print("\n[bold cyan]🛡️ PASSWORD TOOLS[/bold cyan]")
    
    table = Table(title="Password Utilities", show_header=True)
    table.add_column("No", style="cyan", width=5)
    table.add_column("Tool", style="white")
    table.add_column("Description", style="green")
    
    table.add_row("1", "Password Strength Checker", "Check password security")
    table.add_row("2", "Password Generator", "Generate strong passwords")
    table.add_row("3", "Password Hash Generator", "Generate password hashes")
    table.add_row("0", "Back to Main Menu", "Return to main menu")
    
    console.print(table)
    
    choice = Prompt.ask("\n[bold green]Select tool[/bold green]", choices=["1", "2", "3", "0"])
    
    if choice == "1":
        password = Prompt.ask("[+] Enter password to check", password=True)
        strength = validator.check_password_strength(password)
        
        strength_table = Table(title="Password Analysis", show_header=True)
        strength_table.add_column("Metric", style="cyan")
        strength_table.add_column("Status", style="white")
        strength_table.add_column("Score", style="yellow")
        
        for metric, data in strength.items():
            status = "✅" if data['passed'] else "❌"
            strength_table.add_row(metric, status, str(data['score']))
        
        console.print(strength_table)
        console.print(f"[blue]Overall Strength: {strength['overall']['rating']} ({strength['overall']['score']}/100)[/blue]")
        
    elif choice == "2":
        length = int(Prompt.ask("[+] Password length", default="12"))
        include_symbols = Confirm.ask("[+] Include symbols?")
        include_numbers = Confirm.ask("[+] Include numbers?", default=True)
        
        password = validator.generate_password(length, include_symbols, include_numbers)
        console.print(f"[green]🔐 Generated Password: {password}[/green]")
        
    elif choice == "3":
        password = Prompt.ask("[+] Enter password to hash", password=True)
        hash_value = validator.generate_hash(password)
        console.print(f"[blue]🔑 Password Hash (SHA-256): {hash_value}[/blue]")

def file_info_menu():
    """Get file information"""
    console.print("\n[bold cyan]ℹ️ FILE INFORMATION[/bold cyan]")
    
    file_path = Prompt.ask("[+] Enter file path")
    
    if not validator.file_exists(file_path):
        console.print("[red]❌ File not found![/red]")
        return
    
    info = file_handler.get_detailed_file_info(file_path)
    
    info_table = Table(title=f"File Info: {os.path.basename(file_path)}", show_header=True)
    info_table.add_column("Property", style="cyan")
    info_table.add_column("Value", style="white")
    
    for key, value in info.items():
        info_table.add_row(key.replace('_', ' ').title(), str(value))
    
    console.print(info_table)

def main():
    """Main application loop"""
    try:
        banner()
        warning()
        
        while True:
            main_menu()
            choice = Prompt.ask("\n[bold green]Select menu[/bold green]", choices=["1", "2", "3", "4", "5", "0"])
            
            if choice == "1":
                encrypt_file_menu()
            elif choice == "2":
                decrypt_file_menu()
            elif choice == "3":
                batch_encrypt_menu()
            elif choice == "4":
                password_tools_menu()
            elif choice == "5":
                file_info_menu()
            elif choice == "0":
                console.print("[bold red]👋 Goodbye![/bold red]")
                break
            
            if not Confirm.ask("\n[yellow]Continue to main menu?[/yellow]"):
                console.print("[bold red]👋 Goodbye![/bold red]")
                break
                
    except KeyboardInterrupt:
        console.print("\n[bold red]🚪 Exited by user[/bold red]")
    except Exception as e:
        console.print(f"[bold red]💥 Error: {str(e)}[/bold red]")

if __name__ == "__main__":
    # Create necessary directories
    os.makedirs("examples/sample_files", exist_ok=True)
    main()
