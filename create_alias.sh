#!/bin/bash
chmod 755 $HOME/Pytest/pytest
echo alias pytest="$HOME/Pytest/pytest" >> $HOME/.bashrc
echo alias pytest="$HOME/Pytest/pytest" >> $HOME/.zshrc
echo Alias \"pytest\" crée avec succès
