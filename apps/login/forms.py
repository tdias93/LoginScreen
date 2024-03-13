from django import forms

class LoginForms(forms.Form):

    """Formulário para login de usuários.

    Este formulário é usado para coletar informações de login de usuários,
    incluindo nome de usuário (e-mail) e senha. Ele fornece campos formatados
    e estilizados prontos para serem renderizados em uma página HTML.

    Attributes:
        username: Um campo de entrada para o nome de usuário (e-mail) do usuário.
        password: Um campo de entrada para a senha do usuário.

    Example:
        # Instanciando o formulário e renderizando em um template Django
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    """

    # DEFINE O CAMPO DE USUÁRIO
    username = forms.CharField(
        label='E-mail',                              # RÓTULO PARA O CAMPO
        max_length=150,                              # COMPRIMENTO MÁXIMO PERMITIDO PARA A ENTRADA
        widget=forms.TextInput(                      # ESPECIFICA O WIDGET PARA RENDERIZAÇÃO
            attrs={                                  # ATRIBUTOS HTML PARA O ELEMENTO DE ENTRADA
                'class': 'form-control',             # CLASSE CSS PARA ESTILIZAÇÃO
                'placeholder': 'Digite seu e-mail'   # TEXTO DE PLACEHOLDER
            }
        )
    )

    # DEFINE O CAMPO DE SENHA
    password = forms.CharField(
        label='Senha',                             # RÓTULO PARA O CAMPO
        max_length=70,                             # COMPRIMENTO MÁXIMO PERMITIDO PARA A ENTRADA
        widget=forms.PasswordInput(                # ESPECIFICA O WIDGET PARA RENDERIZAÇÃO
            attrs={                                # ATRIBUTOS HTML PARA O ELEMENTO DE ENTRADA
                'class': 'form-control',           # CLASSE CSS PARA ESTILIZAÇÃO
                'placeholder': 'Digite sua senha'  # TEXTO DE PLACEHOLDER
            }
        )
    )