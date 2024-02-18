import os
import time
import random
import threading
import tkinter as tk
from itertools import islice
import base64
import pygame.mixer

Titulo = """
$$$$$$$\                      $$\                        $$\     $$\                         $$\       
$$  __$$\                     $$ |                       $$ |    $$ |                        $$ |      
$$ |  $$ | $$$$$$\  $$$$$$$\  $$ |  $$\        $$$$$$\ $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$$\ $$ |  $$\ 
$$$$$$$\ | \____$$\ $$  __$$\ $$ | $$  |       \____$$  _$$  _|\_$$  _|   \____$$\ $$  _____|$$ | $$  |
$$  __$$\  $$$$$$$ |$$ |  $$ |$$$$$$  /        $$$$$$$ | $$ |    $$ |     $$$$$$$ |$$ /      $$$$$$  / 
$$ |  $$ |$$  __$$ |$$ |  $$ |$$  _$$<        $$  __$$ | $$ |$$\ $$ |$$\ $$  __$$ |$$ |      $$  _$$<  
$$$$$$$  |\$$$$$$$ |$$ |  $$ |$$ | \$$\       \$$$$$$$ | \$$$$  |\$$$$  |\$$$$$$$ |\$$$$$$$\ $$ | \$$\ 
\_______/  \_______|\__|  \__|\__|  \__|       \_______|  \____/  \____/  \_______| \_______|\__|  \__|
"""
Personaje = """
                        .------.
                       / j      ;
                      :.d;       ;
                      $$P        :
           .m._       $$         :
          dSMMSSSss.__$$b.    __ :
         :MMSMMSSSMMMSS$$$b  $$P ;
         SMMMSMMSMMMSSS$$$$     :b
        dSMMMSMMMMMMSSMM$$$b.dP SSb.
       dSMMMMMMMMMMSSMMPT$$=-. /TSSSS.
      :SMMMSMMMMMMMSMMP  `$b_.'  MMMMSS.
      SMMMMMSMMMMMMMMM \  .'\    :SMMMSSS.             
     dSMSSMMMSMMMMMMMM  \/\_/; .'SSMMMMSSSm            
    dSMMMMSMMSMMMMMMMM    :.;'" :SSMMMMSSMM;          
  .MMSSSSSMSSMMMMMMMM;    :.;   MMSMMMMSMMM;           
 dMSSMMSSSSSSSMMMMMMM;    ;.;   MMMMMMMSMMM            
:MMMSSSSMMMSSP^TMMMMM     ;.;   MMMMMMMMMMM            
MMMSMMMMSSSSP   `MMMM     ;.;   :MMMMMMMMM;
"TMMMMMMMMMM      TM;    :`.:    MMMMMMMMM;
   )MMMMMMM;     _/     :`.:    :MMMMMMMM
  d$SS$$$MMMb.  |._\    :`.:     MMMMMMMM
  T$$S$$$$$$$$$$m;O"-;`.:_.-  MMMMMMM;
 :$$$$$$$$$$$$$$$b_l./ ;`.:    mMMSSMMM;
 :$$$$$$$$$$$$$$$$$$$./;`.:  .$$MSMMMMMM
  $$$$$$$$$$$$$$$$$$$$. `.:.$$$$SMSSSMMM;
  $$$$$$$$$$$$$$$$$$$$$. .:$$$$$SSMMMMMMM
  :$$$$$$$$$$$$$$$$$$$$$.//.:$$$$SSSSSSSMM;
  :$$$$$$$$$$$$$$$$$$$$$$.`.:$$SSSSSSSMMMP
"""
print(Titulo, Personaje)
pygame.mixer.init()
pygame.mixer.music.load("OneDrive\Documentos\Tercersemestre\Estructuras II\Parcial 3\Proyecto_Juego\intro.mp3")
pygame.mixer.music.play()

class Juego:
    def dialogos(self, mensaje):
        dialogo = """
                    dS$$S$S$S$S$S$S$$Sb                    
                   :$$S^S$S$S$S$S$S^S$$;                   
                   SSP   `^$S$S$^'   TSS                   
                   $$       `"'       $$                   
                  _SS ,-           -  SS_      ___________________________________            
                 :-.|  _    - .-   _  |.-;    |                                   
                 :\(; ' "-._.'._.-" ` |)/;    |    {}                            
                  \`|  , o       o .  |'/     |                                 
                   ":     -'   `-     ;"      |                                   
                     ;.              :        |                                   
                     : `    ._.    ' ;       /____________________________________            
                   .sSb   ._____.   dSs.                   
                _.d8dSSb.   ._.   .SSbT8b._                
            _.oOPd88SSSS T.     .P SSSS888OOo.             
        _.mMMOOPd888SSSSb TSqqqSP dSSSS88OMOOOMm._         
     .oOMMMOMOOM8O8OSSSSSb TSSSP dSSSSS8OOMMOOMMOOOo._     
   .OOMMOOOMMOOMOOOO  "^SSSTSSP dSSS^"OOOOMMOOMMMOOMMMb.   
  dOOOMMMOMMOOOMOOOO      "^SSSS^"   :OOO8MMMOOMMOOMMOMMb  
 :MMMOOMMOMMOOMMO8OS         `P      8O8OPdMMOOMMOMMOMMMM; 
 MMMMOOMMMMMOOMbTO8S;               :8888MMMMMOMMOMMOMMMMM 
 OMMMMOOMMMMOOOMMOOOS        S     :O8OPdMOMMMOMOMMOOMMMMO 
:OMMMMOOMMOMMOOMbTObTb.     :S;   .PdOPdMOOMMMMMOMMOMMMMMO;
MOOMMMMOMMOMMOOMMMOObTSSg._.SSS._.PdOPdMOOMMMMOMMMMOMMMMOOM
MMOMMMMOMMMOMMOOMMbT8bTSSSSSSSSSPd8OPdOOOMMMMOOMMMMOMMMOOMM
MMOMMMOMMMMMOMMOOMMMbT8bTSSSSSPd88PdOOOOMMMMOOMMMMMMMMOOMMM """.format(mensaje)
        return dialogo.format(mensaje)
    
    def game_over(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        game_over = """ 
        
        
        
        
        
                                                                                                                    
                                             ██████████████          ████████         ██████        █████    ████████████████████ 
                                             ███████████████        █████████         ██████        ██████   ████████████████████ 
                                          ███████                ███████  ██████      █████████  █████████   ██████
                                        █████████              █████████  █████████   ████████████████████   ██████ 
                                        ██████                 ██████        ██████   ████████████████████   ██████████████ 
                                        ██████     █████████   ██████        ██████   ████████████████████   ███████████████
                                        ██████     █████████   ████████████████████   ████████████████████   ███████
                                        ██████▓       ██████   ████████████████████   ██████  ████  ██████   ██████
                                          ▒██████     ██████   ██████        ██████   ██████        ██████   ██████                   
                                           █████████████████   ██████        ██████   ██████        ██████   ████████████████████
                                             ███████████████   ██████        ██████   ██████        ██████   ████████████████████    
                                                
                                                                                                                                                                                                                    
                                           █████████████       ██████        █████    ████████████████████   █████████████████
                                          ███████████████      ██████        ██████   ████████████████████   █████████████████
                                        ██████        ██████   ██████        ██████   ██████                 ██████       ███████ 
                                        ██████        ██████   ██████        ██████   ██████                 ██████       ███████
                                        ██████        ██████   ██████        ██████   ██████████████         ██████       ███████
                                        ██████        ██████   █████████  █████████   ███████████████        ██████     █████████ 
                                        ██████        ██████   ███████████████████    ██████████████         ███████████████████ 
                                        ██████        ██████     ███████████████      ██████                 ███████████████ 
                                        ██████        ██████        █████████         ██████                 ██████  █████████
                                        ███████████████████          ████████         ████████████████████   ██████  ████████████ 
                                          ███████████████              ████           ████████████████████   ██████     █████████ 
                                                                                                                                                    
        """
        print(game_over)
        pygame.mixer.music.stop()
        pygame.mixer.init()
        pygame.mixer.music.load("OneDrive\Documentos\Tercersemestre\Estructuras II\Parcial 3\Proyecto_Juego\Game_Over.mp3")
        pygame.mixer.music.play()
        time.sleep(5)
        exit()
    def win(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        win = """
                                                                                                                                    
                                                  █████       █████    ████████████     █████      █████                       
                                                  ██████     ██████   ██████████████    █████      █████                       
                                                  ██████     ██████  ███████  ███████   █████      █████                       
                                                   ██████   ██████   ██████    ██████   █████      █████                       
                                                    ██████ ██████    ██████    ██████   █████      █████                       
                                                     ███████████     ██████    ██████   █████      █████                       
                                                      █████████      ██████    ██████   █████      █████                       
                                                       ███████       ██████    ██████   █████      █████                       
                                                        █████        ██████    ██████   █████      █████                       
                                                        █████        ██████    ██████   █████      █████                       
                                                        █████        ███████  ███████   ██████    ██████                       
                                                        █████         ██████████████     ██████████████                        
                                                        █████            ████████          ██████████                          
                                                                                                                                
                                                                                                                                
                                                   █████                ██████  ██████   ██████     █████                       
                                                   █████      █████     ██████  ██████   ███████    █████                       
                                                   ██████    ███████   ███████  ██████   ████████   █████                       
                                                    █████    ███████   ██████   ██████   █████████  █████                       
                                                    ██████  █████████ ███████   ██████   ██████████ █████                       
                                                     █████ █████████████████    ██████   ████████████████                       
                                                     ███████████████████████    ██████   █████ ██████████                       
                                                      ██████████ ██████████     ██████   █████  █████████                       
                                                      █████████   █████████     ██████   █████   ████████                       
                                                       ███████     ███████      ██████   █████    ███████                       
                                                       ██████      ███████      ██████   █████    ███████                       
                                                        ████        █████       ██████   █████     ██████                                                                                             
        """
        print(win)
        pygame.mixer.music.stop()
        pygame.mixer.init()
        pygame.mixer.music.load("OneDrive\Documentos\Tercersemestre\Estructuras II\Parcial 3\Proyecto_Juego\win.mp3")
        pygame.mixer.music.play()
        time.sleep(45)
        exit()
        
    def __init__(self, nom):
        self.a = True
        self.nom = nom
        self.vidas = 3
        self.codigo_caja_fuerte = ""
        self.intentos_caja_fuerte = 2
        self.nombre_policia = None
        self.edad_policia = None
        self.altura_policia = None
        self.peso_policia = None

        self.decisiones = {
"inicio": {
    "mensaje": "Buenas tardes {} hemos estado viendo el banco central de Mexico y el de Buenos Aires, \n\t\t\t\t\t\tcreemos que tu eres la mejor opcion para esete atraco. De que mision quieres formar parte?(Mexico, Buenos Aires)".format(self.nom),
    "opciones": {
        "mexico": "Mexico",
        "buenos aires": "Buenos Aires"
    }
},
    "Mexico": {
        "mensaje": "Bienvenido a la mision de Mexico, en esta mision asaltaremos al banco central de Mexico. Para este tenemos opciones de atraco: \n\t\t\t\t\t\t\t- Cavar un tunel \n\t\t\t\t\t\t\t- Asalto a mano armada",
        "opciones": {
            "tunel":  "tunel",
            "mano": "mano"
        }
            },
        "tunel": {
            "mensaje": "Has elegido cabar un tunel, ahora puede que los caluclos fallen, puedes ver el mapa o seguir",
            "opciones": {
                "mapa": self.mapa,
                "seguir": "laverinto"
            }
            },
            
                "laverinto":{
                    "mensaje": "Es momento de iniciar el atraco, no sabemos con exactitud donde saldra el tunel asi que tienes que estar preparado para todo, escribe vamos",
                    "opciones": 
                    {
                        "vamos":  self.laverinto,
                        "seguir": "Camaras",
                    }
                },
                    "Camaras":{
                        "mensaje": "Hemos salido del laberinto, es hora de dirigirnos a la caja fuerte pero hay que pasar por desapercibido,\n\t\t\t\t\t\t\t por lo tanto intentaremos no ser vistos por las camaras, escribe 'adelante' para continuar",
                        "opciones": 
                        {
                            "adelante": self.minijuego_0,
                            "seguir": "Desifrar",
                        }
                    },

                        "Desifrar":{
                            "mensaje": "Hemos pasado las cámaras de las oficinas, ahora para continuar con el atraco, debemos pasar por las cajas,\n\t\t\t\t\t\t\tel problema es que la puerta tiene un código que debemos descubrir escribe 'adivinar' para acceder al proceso",
                            "opciones":
                            {
                                "adivinar": self.minijuego_1,
                                "seguir": "Cajas"
                            }
                        },

                            "Cajas": {
                                "mensaje": "Listo, has llegado a las cajas para continuar las tendrás que asaltar y conseguir dinero, escribe 'asaltar' para continuar",
                                "opciones":
                                {
                                    "asaltar": self.minijuego_2,#OJO
                                    "seguir": "Donde"
                                }
                            },

                                "Donde": {
                                    "mensaje": "Has pasado la sección de cajas exitosamente, pero hay un problema, se te ha olvidado el mapa y no sabes a donde ir,\n\t\t\t\t\t\tno sabes si es a la izquierda, a la derecha, arriba o abajo, si viste el mapa al inicio esto será facil para ti.\n\t\t\t\t\t\tA donde te diriges?",
                                    "opciones":
                                    {
                                        "abajo": self.decifrar_caja_fuerte,
                                        "izquierda": self.perder_vida,
                                        "arriba": self.perder_vida,
                                        "derecha": self.perder_vida,
                                        "regresar": "Donde"
                                    }
                                },
        "mano": {
            "mensaje": "Haz elegido hacer el atraco a mano armada, por lo que se te asignara un sufusil, quieres ver el mapa antes de entrar o quieres seguir?",
            "opciones": {
                "mapa": self.mapa2,
                "seguir": "Atraco"
            }
        },

            "Atraco": {
                "mensaje": "Perfecto, has llegado por la entrada principal y disparas alteradamente hacía el techo para avisar que llegaste jeje,\n\t\t\t\t\t\t\tAhora te diriges a las cajas, escribe 'continuar'",
                "opciones":{
                    "continuar": self.minijuego_mano_0,
                    "seguir": "Pasillo"
                }
            },

                "Pasillo": {
                    "mensaje": "Excelente, después de sacar un poco de dinero ahora te encuentras en un pasillo lleno de cámaras y para llegar a la bóbeda\n\t\t\t\t\t\t\t a fuerzas tienes que pasar por el, escribe 'vamos' para avanzar por el pasillo",
                    "opciones":{
                        "vamos": self.minijuego_mano_1,
                        "avanzar": "Oficinas"
                    }
                },

                    "Oficinas":{
                        "mensaje": "Pasaste el pasillo exitosamente, ahora has llegado a las oficinas y hay un grupo de policias,\n\t\t\t\t\t\t\t en esta ocasión tendrás que dispararles, escribe 'disparar' para empezar el juego",
                        "opciones": {
                            "disparar": self.minijuego_mano_2,
                            "regresar": "Ejecutivo"
                        }
                    },

                        "Ejecutivo":{
                            "mensaje": "Felicidades, le has disparado a todos los policias, ahora vamos a la última sección para abrir la bóveda, escribe 'continuar'",
                            "opciones":{
                                "continuar": self.minijuego_mano_3,
                                "regresar": "BombaOculta"
                            }
                        },

                            "BombaOculta":{
                                "mensaje": "Excelente, ahora tienes que pasar la sección de seguridad para poder abrir la bóveda, escribe 'avanzar' para ir a la última sección",
                                "opciones":{
                                    "avanzar": self.minijuego_mano_4,
                                    "decifrar": self.decifrar_caja_fuerte_mano
                                }
                            },

"Buenos Aires": {
    "mensaje": "Che {} bienvenido a la mision de atraco de Buenos Aires, para este atracto tenemos dos opciones: \n\t\t\t\t\t\t\t - Modo sigiloso \n\t\t\t\t\t\t\t - Hackea la base de datos".format(self.nom),
    "opciones": {
        "sigiloso":  "Sigiloso",
        "hack": "hack"
    }
            },

        "Sigiloso": {
            "mensaje": "Has decidido el modo sigiloso, para esta opción tendrás que infiltrarte en el banco, te infiltraras vistiendote de policia\n\t\t\t\t\t\t\t para crear tu identificación falsa escribe 'policia'",
            "opciones": {
                "policia":  self.identificacion_falsa,
                "listo": "Policia"
            }
        },

                "Policia": {
                "mensaje": "Después de ver los datos del policia, entras y nadie nota nada, caminas y llegas a las cajas,\n\t\t\t\t\t\t\t ahora tienes que corroborar que las cajas con su cantidad respectiva de dinero escribe 'checar' para continuar ",
                "opciones": {
                    "checar":  self.checar,
                    "continuar": "Checar"
                }
            },

                    "Checar": {
                    "mensaje": "Perfecto, ahora caminas por un pasillo lleno de cámaras, pero como eres policias no pasa nada, escribe 'caminar' para avanzar",
                    "opciones": {
                        "caminar":  self.caminar,
                        "entrar": "Ofice"
                    }
                },

                        "Ofice": {
                            "mensaje": "Te encuentras en las oficinas y hay muchos policias, tienes que hablar con ellos para disimular tu falsa identidad, escribe 'hablar' para continuar",
                            "opciones": {
                                "hablar":  self.hablar,
                                "seguir": "Ejec"
                            }
                        },

                            "Ejec": {
                            "mensaje": "Te encontraste con el ejecutivo, el reconoce siempre a todos, pero como tu eres infiltrado, te llama,\n\t\t\t\t\t\t\t te quita tu identificación y te pregunta tus datos. Escribe 'datos' para responderle",
                            "opciones": {
                                "datos":  self.datos,
                                "seguir": "Seguri"
                            }
                        },

                                "Seguri": {
                                "mensaje": "Entraste a Seguridad, la última parte del banco, escribe 'vamos' para avanzar",
                                "opciones": {
                                    "vamos":  self.cables,
                                    "decifrar": self.decifrar_caja_fuerte #AQUI
                                }
                            },

        "hack": {
            "mensaje": "Has decidido la opcion de hackear la base de datos del banco, para esto iremos buscando partes de la \n\t\t\t\t\t\t\tcontraseña para poder acceder a la base de datos, escribe seguir para continuar",
            "opciones": {
                "seguir":  "reglas",
                "hack": "hack"
                }
            },
            "reglas": {
                "mensaje": "Como Has decidido ser un hacker, vas a tener que desifrar codigos para poder acceder a la contraseña, estas listo para empezar a decifrar?",
                "opciones": {
                    "si":  self.minh1,
                    "seguir": "juego 2"
                    }
                },
                "juego 2": {
                    "mensaje": "Excelente ya has podido pasar la promer prueba, esperemos seguir asi y que no nos encuentre, pero tenemos que actuar rapido, \n\t\t\t\t\t\t\t presiona la tecla t para seguir decifrando",
                    "opciones": {
                        "t":  self.minh2,
                        "r": "juego 3"
                        }
                    },
                    "juego 3": {
                        "mensaje": "Excelente, acaso llevas clases con Manuel? O Por que eres tan bueno? ",
                        "opciones": {
                            "si":  "con razon",
                            "no": "deberias",
                            "tal": "con razon",
                            "jaja": "deberias",
                            "maybe": "deberias",
                            "se": "con razon"
                            }
                        },
                        "con razon": {
                            "mensaje": "Muy bien tu si sabes lo que es bueno, por eso te damos dos opciones: x para jugar el siguiente juego, y para salterte el juego",
                            "opciones": {
                                "x":  self.minh3,
                                "y": "pass",
                                "m": self.minh4
                                }
                            },
                        "deberias": {
                            "mensaje": "Pues deberias, no sabes lo que te pierdes, pero bueno es momento de seguir, presiona x ",
                            "opciones": {
                                "x":  self.minh3,
                                "m": "juego 4"
                                }
                            },
                             "pass": {
                                "mensaje": "Has decidido saltarte al siguiente nivel, por lo que te daremos la contraseña: 'de', escribe 'x' para continuar",
                                "opciones": {
                                    "x":  self.minh4,
                                    "si": self.win,
                                    "no": "que"
                                    }
                                },
                            "juego 4": {
                                "mensaje": "Esta es tu ultima prueba, y por cierto la mas dificil, ya estas cerca de llegar al final, escribe listo para empezar",
                                "opciones": {
                                    "listo":  self.minh4,
                                    "si": self.win,
                                    "no": "que"
                                    }
                                },
                                "que": {
                                    "mensaje": "Venga, esta ya es la ultima vez que preguntamos estas cerca de ganar, vuelve a contestar la pregunta",
                                    "opciones": {
                                        "si": self.win,
                                        "no": "como"
                                        }
                                    },
                                "como": {
                                    "mensaje": "Reconcideralo una vez mas, venga estamos a una sola palabra",
                                    "opciones": {
                                        "si": self.win,
                                        "no": "que"
                                        }
                                    },
            "fin": {
                "mensaje": "El juego ha terminado. ¿Quieres jugar de nuevo?",
                "opciones": {
                    "si": "inicio",
                    "no": None
                }
            }
        }
        self.estado_actual = "inicio"


    def mostrar_dialogo(self, mensaje, mostrar_art=True): #DUDA, QUE ES MOSTRAR_ART ?
        os.system('cls' if os.name == 'nt' else 'clear')
        if mostrar_art:
            print(self.dialogos(mensaje))
        else:
            print(mensaje)

    def jugar(self):
            if self.a == True:
                self.a = False
                pygame.mixer.init()
                pygame.mixer.music.load("OneDrive\Documentos\Tercersemestre\Estructuras II\Parcial 3\Proyecto_Juego\Reloj.mp3")
                pygame.mixer.music.play()

            decision = self.decisiones[self.estado_actual]
            self.mostrar_dialogo(decision["mensaje"])
            while True:
                respuesta = input().lower() 
                for opcion, estado in decision["opciones"].items():
                    if opcion in respuesta:
                        if callable(estado):  # Verifica si es una función antes de llamarla
                            estado()
                        else:
                            # Verifica y actualiza las vidas después de cada decisión
                            if "vidas" in decision: #PORQUE PONE VIDAS EN COMILLAS ?
                                self.vidas += decision["vidas"]
                            
                            # Verifica si se ha agotado el número de vidas
                            if self.vidas <= 0:
                                print("Has perdido todas tus vidas. ¡Fin del juego!")
                                self.estado_actual = None
                                print(self.game_over())
                                break
                            else: 
                                self.estado_actual = estado
                                decision = self.decisiones[self.estado_actual]
                                self.mostrar_dialogo(decision["mensaje"])

                        break
                if not self.estado_actual:
                    break
    
    def j(self):
        print("hola")
        
    def mapa2(self):
        print("Este será el mapa del banco, no te lo podras llevar por lo que te lo tienes que aprender")
        mapa = """
                                                                                                            
          ████████████████████████████████████████████████████████████████████████████████████████████            
          █ ██                             ███           █        █                               █               
          █ ██                             ███           █        █                               █               
          █ ██                             ███           █        █               █               █               
          █ ██                             ███           █        █               █               █               
          █ ██       Bobeda                ███           █        █               █               █            
          █ ██                             ███                                    █               █               
          █ ██                             ███             Cajas                  █              ██████████         
          █ ██                             ███                                    █                            
          █ ███████ ████████ █████████████████      ███████████████████████████████                Entrada                
          █ ██      ████████               ███                                  ███               principal                  
          █ ██      ████████               ███             Pasillo              ███                                   
          █ ██                             ███                                  ███              ██████████              
          █ ██                             ██████████████████████████████       ███████████████████████████               
          █ ██                                                █                                   █               
          █ ██        Seguridad                               █                                   █                
          █ ██                             ███                █                                   █
          █ ██                             ███    ejecutivo   █             oficinas              █        
          █ ██                             ███                █                                   █               
          █ ██                             ███                █                                   █               
          █ ██                             ███                                                    █               
          █████████████████████████████████████████████████████████████████████████████████████████                                                                          
        """
        print(mapa)
        print("Escribe seguir para avanzar")
    
    def mapa(self):
        print("Este será el mapa del banco, no te lo podras llevar por lo que te lo tienes que aprender")
        mapa = """
                                                                                                            
          ████████████████████████████████████████████████████████████████████████████████████████████            
          █ ██                             ███           █        █                               █               
          █ ██                             ███           █        █                               █               
          █ ██                             ███           █        █               █               █               
          █ ██                             ███           █        █               █               █               
          █ ██      #No se como ponerle                  █        █               █               █            
          █ ██                                                                    █               █               
          █ ██                             ███             cajas                  █              ██████████         
          █ ██                             ███                                    █                            
          █ ███████████████████████████████████████      ██████████████████████████                Entrada                
          █ ██                            █████████   Entrada                   ███                principal                  
          █ ██                            █████████    a la                     ███                                   
          █ ██                            █████████   bobeda                    ███              ██████████              
          █ ██                            ██████████████████████████████████████████      █████████               
          █ ██                             ███                █                                   █               
          █ ██           Bobeda            ███                █                                   █                
          █ ██                             ███                █                                   █
          █ ██                             ███    ejecutivo   █             oficinas              █        
          █ ██                             ███                █                                   █               
          █ ██                             ███                █                                   █               
          █ ██                             ███                                                    █               
          █████████████████████████████████████████████████████████████████████████████████████████                                                                          
        """
        print(mapa)
        print("Escribe seguir para avanzar")
        
    def laverinto(self):
        laverinto = """
           ██████████████████████████████████████████████████████████████████████████████           
           ██████████████████████████████████████████████████████████████████████████████           
           ███                      ███                                               ███           
           ███                      ███                                    k          ███           
           ███                      ███                                               ███           
           ███     ████████████     ███     █████████████████████████████     ███████████           
           ███             ████             ███                      ████     ███                   
           ███     p       ████    i    j   ███                      ████     ███    salida               
           ███             ████             ███                      ████     ███                   
           ████████████████████     ████████████████████████████     ████████████     ███           
           ████████████████████     ████████████████████████████     ████████████     ███           
           ███             ████                              ███                      ███           
           ███             ████    g                         ███  q                y  ███           
           ███             ████                           r  ███                      ███           
           ███     ███     ████     ████████████████████     ███     ████████████     ███           
           ███     ███     ████     ████████████████████     ███     ████████████     ███           
           ███     ███     ████     ███              ███     ███     ████     ███     ███           
           ███     ███     ████     ███              ███     ███     ████     ███     ███           
           ███     ████████████████████     ███      ███     ███     ████     ███     ███           
           ███     ████████████████████     ███      ███     ███     ████     ███     ███           
                                            ███      ███     ███     ████     ███     ███           
       Entrada   a               b          ███      ███     ███     ████     ███     ███           
                                            ███      ███     ███     ████     ███     ███           
           ████████████████████     ███████████      ███     ███     ████     ███████████           
           ████████████████████     ███████████      ███     ███     ████     ███████████           
           ███                      ███                      ███     ████             ███           
           ███                  c   ███           f          ███     ████          c  ███           
           ███      ██████████      ███████████      ███     ███     ███████████      ███           
           ███     ████████████     ███     ███      ███     ███     ████████████     ███           
           ███     ███              ███     ███      ███     ███              ███     ███           
           ███     ███              ███     ███      ███     ███              ███     ███           
           ███     ███              ███     ███      ███     ███              ███     ███           
           ███  h  ████████████████████     ███      ████████████████████     ███     ███           
           ███     ████████████████████     ███      ████████████████████     ███     ███           
           ███     ███              ███     ███                               ███     ███           
           ███     ███              ███     ███                             m ███     ███           
           ███     ███              ███     ███                               ███     ███           
           ███     ████████████     ███     █████████████████████████████     ███     ███           
           ███                                               ███                      ███           
           ███                   d        e                  ███                      ███           
           ███                                               ███                      ███           
           ██████████████████████████████████████████████████████████████████████████████           
           ██████████████████████████████████████████████████████████████████████████████ 
        """
        print(laverinto)
        print("Has salido por la oficinas, pero te has quedado atorado, es momento de salir")
        print("Escribe la letra a la que te quieres dirigir")
        print("Intentos restantes:", self.vidas)
        c = input("Inicias en 'a' a donde vas?")
        if self.vidas -1 > 0:
            if c  == "b":
                    d = input("Estas en 'b' a donde vas?")
                    if d == "f":
                            e = input("Estas en 'f' a donde vas?")
                            if e == "m":
                                    f = input("Estas en 'm' a donde vas?")
                                    if f == "q":
                                            g = input("Estas en 'q' a donde vas?")
                                            if g == "y":
                                                print("Has salido de las oficinas Felicidades, escribe 'seguir' para continuar")
                                                x = random.randint(0,9)
                                                print("El número de esta sección es el:", x)
                                                self.codigo_caja_fuerte += str(x)
                                            else:
                                                self.vidas -= 1
                                                print("Intentalo una vez mas")
                                                self.laverinto()
                                    else:
                                            self.vidas -= 1
                                            print("Intentalo una vez mas")
                                            self.laverinto()
                            else:
                                    self.vidas -= 1
                                    print("Intentalo una vez mas")
                                    self.laverinto()
                    else:
                            self.vidas -= 1
                            print("Intentalo una vez mas")
                            self.laverinto()
            else: 
                    self.vidas -= 1
                    print("Intentalo una vez mas")
                    self.laverinto()          
        else:
            self.game_over()
        

    def perder_vida(self):
        self.vidas -= 1
        if self.vidas == 0:
            self.game_over()
        else:
            print("Perdiste una vida, te quedan:", self.vidas, "escribe 'regresar'")
    
    def minijuego_0(self):
        print("\nLlegaste a un pasillo donde hay cámaras que cambian de lado cada 2 segundos, primero apuntan\na la izquierda y luego a la derecha pero si te pones abajo de la cámara la evitarás")
        print("\nInstrucciones: Tendrás que escribir el número de pasos exactos para estar debajo de la cámara para que así no te vea")
        print("\nEjemplo: La camara esta apuntando a la izquierda, tu tendrás que escribir la palabra 'esperar' de lo contrario la cámara de verá,\n         después de 2 segundos la cámara apuntará a la derecha y es entonces cuando podrás moverte.")
        print("         Si la camara apuntaba en un rango de 1 - 5 darás entonces 6 pasos para quedar abajo y cuando la cámara apunte de nuevo a la \n         izquierda ya podrás moverte, pero ten en cuenta los pasos que darás porque después de una cámara sigue otra")
        print("\nTienes 3 intentos, si no pierdes una vida")
        game = Juego(None)
        a = self.vidas
        class ej():
            def __init__(self):
                self.vidas = a
                self.intentos = 3
            def caso_base(self):
                ini = 1
                fin = random.randint(2,10)
                ini2 = fin + 2
                fin2 = random.randint(ini2+1, ini2+11)
                
                ini3 = fin2 + 1
                fin3 = random.randint(ini3+1, ini3+11)

                ini4 = fin3 + 2
                fin4 = random.randint(ini4+1, ini4+11)
                return ini, fin, ini2, fin2, ini3, fin3, ini4, fin4

            def case1(self,a, b, ini, fin, ini4, fin4):
                print("-->La camara", a, "apunta a la izquierda con un rango de: ", ini, "-", fin)
                print("-->La camara", b, "apunta a la derecha con un rango de:", ini4, "-", fin4)
                respuesta = input("Si vas a avanzar escribe el número de pasos, de lo contrario escribe 'esperar': ")
                while respuesta != "esperar" and not respuesta.isdigit():
                    print("Respuesta no válida, intenta de nuevo")
                    respuesta = input("Si vas a avanzar escribe el número de pasos, de lo contrario escribe 'esperar': ")
                if respuesta != 'esperar': 
                    if int(respuesta) > fin3 and int(respuesta) < ini4:
                        print("\nListo, avanzaste", respuesta, "pasos")
                        print("{ Te encuentras abajo de la cámara", b, "}")
                    else:
                        self.intentos -= 1
                        if self.intentos == 0:
                            print("Ya fueron 3 intentos, debes continuar, pero perderás una vida,\nTus vidas:", self.vidas-1)
                            self.vidas -= 1
                            if self.vidas == 0:
                                game.game_over()
                            self.intentos = 3
                        else: 
                            print("¡¡¡La cámara te vio, te quedan", self.intentos, "oportunidades para no perder vidas!!!")
                        print("Vuelve a intentarlo, sigues abajo de la cámara", a)
                        self.case1(a, b, ini, fin, ini4, fin4)
                elif respuesta == 'esperar':
                    print("Bien, ahora espera a que giren las cámaras para poder avanzar")
                    time.sleep(3)
                    print()
                    print("Listo, las camaras han cambiado")

            def case2(self, a, b, ini2, fin2, ini3, fin3):
                print("-->La camara", a, "apunta a la derecha con un rango de:", ini2, "-", fin2)
                print("-->La camara", b, "apunta a la izquierda con un rango de:", ini3, "-", fin3)
                respuesta = input("Si vas a avanzar escribe el número de pasos, de lo contrario escribe 'esperar': ")
                while respuesta != "esperar" and not respuesta.isdigit():
                    print("Respuesta no válida, intenta de nuevo")
                    respuesta = input("Si vas a avanzar escribe el número de pasos, de lo contrario escribe 'esperar': ")
                if respuesta != 'esperar':
                    if int(respuesta) > fin and int(respuesta) < ini2:
                        print("\nListo, avanzaste", respuesta, "pasos")
                        print("{ Te encuentras abajo de la camara", a, "}")
                    else:
                        self.intentos -= 1
                        if self.intentos == 0:
                            print("Ya fueron 3 intentos, debes continuar, pero perderás una vida,\nTus vidas:", self.vidas-1)
                            self.vidas -= 1
                            if self.vidas == 0:
                                game.game_over()
                            self.intentos = 3
                        else:
                            print("¡¡¡La cámara te vio, te quedan,", self.intentos, "oportunidades para no perder vidas!!!")
                        print("Vuelve a intentarlo, sigues abajo de la cámara", b)
                        self.case2(a, b, ini2, fin2, ini3, fin3)
                elif respuesta == 'esperar':
                    print("Bien, ahora espera a que giren las cámaras para poder avanzar")
                    time.sleep(3)
                    print()
                    print("Listo, las camaras han cambiado")
            
            def case4(self, b):
                print("La camara", b, "apunta a la izquierda")
                a = input("Escribe 'avanzar' para pasar la última cámara")

        ob = ej()
        ini, fin, ini2, fin2, ini3, fin3, ini4, fin4 = ob.caso_base()
        print("{Te encuentras al inicio del pasillo}")
        a = 1
        b = 2
        s = 0
        while(self.vidas > 0):
            ob.case1(a,b,ini, fin, ini4, fin4)
            ob.case2(a,b,ini2, fin2, ini3, fin3)
            ob.case1(a,b,ini, fin, ini4, fin4)
            ini, fin, ini2, fin2, ini3, fin3, ini4, fin4 = ob.caso_base()
            s+= 1
            if s == 4:
                ob.case4(b)
                break
            a += 1
            b += 1
        print("Felicidadeeees")
        x = random.randint(0,9)
        print("El número de esta sección es el:", x)
        self.codigo_caja_fuerte += str(x)
        print("Escribe 'seguir' para continuar")

    def minijuego_1(self):
        print("Instrucciones: Para saber que código es el correcto tendrás que adivinar en cual de las 6 cajas se encuentra el número")
        print("Pista: son 5 digitos y si su posicion es impar se encuentra en una caja de posicion impar, lo mismo para posiciones pares")
        print("Ejemplos: el tercer digito podría encontrarse en la caja 1, 3 o 5")
        print("Tienes 4 intentos por digito")

        cajas = """
                ████████      ████████      ████████    
                ██  1 ██      ██  2 ██      ██  3 ██
                ████████      ████████      ████████

                ████████      ████████      ████████    
                ██  4 ██      ██  5 ██      ██  6 ██
                ████████      ████████      ████████
                """
        lista = ""
        i = 1
        intentos = 4
        while i < 6:
            print(cajas)
            x = random.randint(0, 9)
            lista += str(x)
            if i % 2 != 0:
                y = random.randrange(1, 6, 2)
                #print(y)
                a = 0
                while a != y:
                    a = input("En que caja crees que esté el dígito? ")
                    if int(a) == y:
                        intentos = 4
                        print("El digito", i, "es:", x)
                        i += 1
                        break
                    else:
                        intentos -= 1
                        print("Incorrecto, te quedan", intentos, "intentos")
                    if intentos == 0:
                        print("SE ACTIVÓ LA ALARMA Y ALERTASTE A LOS POLICIAS...")
                        self.game_over()
            else:
                y = random.randrange(2, 7, 2)
                #print(y)
                a = 0
                while a != y:
                    a = input("En que caja crees que esté el dígito?")
                    if int(a) == y:
                        intentos = 4
                        print("El digito", i, "es:", x)
                        i += 1
                        break
                    else:
                        intentos -= 1
                        print("Incorrecto, te quedan", intentos, "intentos")
                    if intentos == 0:
                        print("SE ACTIVÓ LA ALARMA Y ALERTASTE A LOS POLICIAS...")
                        self.game_over()
            input("Presiona enter después de que anotes o te memorices el dígito")
            os.system('cls' if os.name == 'nt' else 'clear')
        
        p = input("Escribe el número que econtraste en las cajas: ")
        if p == lista:
            print("Felicidadeeeees")
        else:
            print("SE ACTIVÓ LA ALARMA Y ALERTASTE A LOS POLICIAS...")
            time.sleep(2)
            self.game_over()
        #print(lista)       
        print("Escribe 'seguir' para continuar con la misión")
        x = random.randint(0,9)
        print("El número de esta sección es el:", x)
        self.codigo_caja_fuerte += str(x)

    def minijuego_2(self):
        duracion_ciclo = 20

        print("Listo, ahora vas a asaltar las cajas")
        print("Instrucciones: Se te daran palabras, y tu tendras que escribirlas, si te equivocas en una palabra no importa, puedes continuar con la siguiente palabra mientras no se te acabe el tiempo")
        print("Entre más palabras escribas más dinero obtendrás")

        class Temporizador(threading.Thread):
            def __init__(self, duracion):
                super().__init__()
                self.duracion = duracion
                self.terminado = threading.Event()

            def run(self):
                time.sleep(self.duracion)
                self.terminado.set()

        class Lector(threading.Thread):
            def __init__(self):
                super().__init__()
                self.palabra = ""
                self.respuesta = None
                self.contador = 0

            def run(self):
                while not temporizador.terminado.is_set():
                    for _ in range(7):
                        x = random.randint(97, 122)
                        letra = chr(x)
                        self.palabra += letra
                    print("Escribe la palabra:", self.palabra)
                    self.respuesta = input()
                    if self.respuesta.lower() == self.palabra:
                        self.contador += 1
                        print("Bieeeeen")
                    else:
                        tiempo = int(duracion_ciclo - (time.time() - tiempo_inicio))
                        if tiempo >= 0:
                            print("Palabra incorrecta\t Te quedan:", tiempo, "segundos")
                    self.respuesta = None
                    self.palabra = ""

        temporizador = Temporizador(duracion_ciclo)
        lector = Lector()

        inpu = 'a'
        while inpu != 's':
            inpu = input("Para comenzar presiona la letra s\n")
            if inpu == 's':
                temporizador.start()
                lector.start()
                tiempo_inicio = time.time()

        while not temporizador.terminado.is_set():
            continue

        if temporizador.terminado.is_set():
            print()
            print("Se acabó el tiempo")
        dinero_robado = lector.contador * 19999
        print("Lograste robar $", dinero_robado)
        if dinero_robado != 0:
            x = random.randint(0,9)
            print("El número de esta sección es el:", x)
            self.codigo_caja_fuerte += str(x)
        else:
            print("No robaste nada, no te podemos dar el número, tendrás que adivinarlo al final")
        print("Da enter y escribe 'seguir' para continuar el asalto") 

    def decifrar_caja_fuerte(self):
        def botton_1():
            x = int(label1.cget("text")) + 1
            if x == 10:
                x = 0
            x = str(x)
            label1.config(text=x)
        def botton_2():
            x = int(label2.cget("text")) + 1
            if x == 10:
                x = 0
            x = str(x)
            label2.config(text=x)
        def botton_3():
            x = int(label3.cget("text")) + 1
            if x == 10:
                x = 0
            x = str(x)
            label3.config(text=x)
        def botton_4():
            x = int(label4.cget("text")) + 1
            if x == 10:
                x = 0
            x = str(x)
            label4.config(text=x)
        def botton_5():
            x = int(label1.cget("text"))
            if x == 0:
                x = 9
            else:
                x -= 1
            x = str(x)
            label1.config(text=x)
        def botton_6():
            x = int(label2.cget("text"))
            if x == 0:
                x = 9
            else:
                x -= 1
            x = str(x)
            label2.config(text=x)
        def botton_7():
            x = int(label3.cget("text"))
            if x == 0:
                x = 9
            else:
                x -= 1
            x = str(x)
            label3.config(text=x)
        def botton_8():
            x = int(label4.cget("text"))
            if x == 0:
                x = 9
            else:
                x -= 1
            x = str(x)
            label4.config(text=x)

        def botton_9():
            numero = ""
            numero += label1.cget("text")
            numero += label2.cget("text")
            numero += label3.cget("text")
            numero += label4.cget("text")
            if numero == self.codigo_caja_fuerte:
                print("Felicidaaaaadeeeeees!!!!!!, Lograste entrar a la caja fuerte")
                print("Fin del juego")
                ventana.destroy()
                self.win()
            else:
                ventana.destroy()
                if self.intentos_caja_fuerte > 0:
                    self.intentos_caja_fuerte -= 1
                    print("Ese no es el número, te quedan", self.intentos_caja_fuerte, "más")
                    self.decifrar_caja_fuerte()
                else:
                    print("Se acabaron tus intentos")
                    self.game_over()

        # Crear la ventana principal
        ventana = tk.Tk()
        ventana.title("")

        contenedor0 = tk.Frame(ventana)
        contenedor0.pack(expand=True)

        # Crear un botón
        button1 = tk.Button(contenedor0, text="^", command=botton_1)
        button1.grid(row=0, column=0, padx=25, pady=20)

        button2 = tk.Button(contenedor0, text="^", command=botton_2)
        button2.grid(row=0, column=1, padx=25, pady=20)

        button3 = tk.Button(contenedor0, text="^", command=botton_3)
        button3.grid(row=0, column=2, padx=25, pady=20)

        button4 = tk.Button(contenedor0, text="^", command=botton_4)
        button4.grid(row=0, column=3, padx=25, pady=20)


        contenedor1 = tk.Frame(ventana)
        contenedor1.pack(expand=True)

        # Crear un etiqueta
        label1 = tk.Label(contenedor1, text="0")
        label1.grid(row=0, column=0, padx=28, pady=20)

        label2 = tk.Label(contenedor1, text="0")
        label2.grid(row=0, column=1, padx=28, pady=20)

        label3 = tk.Label(contenedor1, text="0")
        label3.grid(row=0, column=2, padx=28, pady=20)

        label4 = tk.Label(contenedor1, text="0")
        label4.grid(row=0, column=3, padx=28, pady=20)

        contenedor2 = tk.Frame(ventana)
        contenedor2.pack(expand=True)

        # Crear un botón
        button5 = tk.Button(contenedor2, text="v", command=botton_5)
        button5.grid(row=0, column=0, padx=25, pady=20)

        button6 = tk.Button(contenedor2, text="v", command=botton_6)
        button6.grid(row=0, column=1, padx=25, pady=20)

        button7 = tk.Button(contenedor2, text="v", command=botton_7)
        button7.grid(row=0, column=2, padx=25, pady=20)

        button8 = tk.Button(contenedor2, text="v", command=botton_8)
        button8.grid(row=0, column=3, padx=25, pady=20)

        contenedor3 = tk.Frame(ventana)
        contenedor3.pack(expand=True)

        botton9 = tk.Button(contenedor3, text="Aceptar", command=botton_9)
        botton9.grid(row=0, column=3, padx=25, pady=20)

        # Iniciar el bucle principal de la interfaz gráfica
        ventana.mainloop()





    def minijuego_mano_0(self):
        class ClickGame:
            def __init__(self, ventana):
                self.ventana = ventana
                self.ventana.title("Click Game")

                self.label = tk.Label(ventana, text="Haz clic en el botón")
                self.label.pack(pady=10)

                self.button = tk.Button(ventana, text="¡Clic aquí!", command=self.on_button_click)
                self.button.pack(pady=20)

                self.click_count = 0
                self.start_time = None
                self.click_count2 = 0
                self.start_time2 = None

            def on_button_click(self):
                if self.start_time is None:
                    self.start_time = time.time()
                    self.ventana.after(10000, self.change_botton)  # Juego de 10 segundos
                self.click_count += 1
            
            def change_botton(self):
                self.button.config(state=tk.DISABLED)  
                self.button2 = tk.Button(ventana, text="¡Clic aquí!", command=self.on_button_click)
                self.button2.pack(padx = 30, pady=20)
                if self.start_time2 is None:
                    self.start_time2 = time.time() 
                    self.ventana.after(10000, self.end_game)  # Juego de 10 segundos
                self.click_count2 += 1

            def end_game(self):
                cps = self.click_count + self.click_count2  # Clics por segundo
                self.label.config(text= "Fin del juego\nClics totales: " + str(cps))
                self.button2.config(state=tk.DISABLED)  # Desactivar el botón después del juego
                print("Felicidades, pasaste las cajas y robaste $", cps*1999)

        if __name__ == "__main__":
            ventana = tk.Tk()
            game = ClickGame(ventana)
            ventana.mainloop()
        print("Escribe 'seguir' para continuar")


    def mover_jugador(self, posicion_jugador, pasos):
        return posicion_jugador + pasos

    def detectar_camara(self, posiciones_camaras, posicion_jugador):
        for posicion_camara in posiciones_camaras:
            if posicion_camara in range(posicion_jugador, posicion_jugador + 1 ):
                return True
        return False

    def minijuego_mano_1(self):
        posicion_jugador = 0
        rango_vision = 10
        pasos_totales = 0
        contador_multiplo = 5
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n\nHas logrado pasar por cajas, pero se acerca el pasillo donde hay mayor vigilancia, vas a tener que escabar de las camaras de suguridad")
        print("\tPara ello hemos tomado un registro de la ubicacion de las camaras de suguridad, y hemos notado que tienen un patron ")
        print("\tla primer camara se encuentra a un rango de 2 pasos, cuando rebases los 20 pasos, te enontraras con una camara cada 3 pasos")
        print("\t al rebasar los 38 pasos te encontras con una camra cada 5 pasos, finalmente al rebasar los 63 pasos te encontraras con una camara cada 7 pasos")
        print("\t¡Cuidado! si te detectan te atraparan y perderas una vida en el juego\n\n")
        
        while True:
            posiciones_camaras = list(range(0, 20, 2)) + list(range(20, 38, 3)) + list(range(38, 63, 5)) + list(range(63, 85, 7))
            
            pasos = int(input("¿Cuántos pasos quieres moverte? "))
            posicion_jugador = self.mover_jugador(posicion_jugador, pasos)
            pasos_totales += pasos
            
            if self.detectar_camara(posiciones_camaras, posicion_jugador):
                print("¡Has sido atrapado por una cámara de seguridad!")
                self.vidas -= 1
                self.game_over()
                return    
                
            if pasos_totales < 20:
                print("Sigues en un rango de camara por cada dos pasos")
            elif pasos_totales > 20 and pasos_totales < 38:
                print("Ahora estas en un rango de camara por cada tres pasos")
            elif pasos_totales > 38 and pasos_totales < 63:
                print("Ahora estas en un rango de camara por cada cinco pasos")
            elif pasos_totales > 63 and pasos_totales < 84:
                print("Ahora estas en un rango de camara por cada siete pasos")

            if pasos_totales >= 80:
                print("¡Felicidades! Has dado", pasos_totales, "pasos sin ser atrapado por una cámara de seguridad.")
                print("Escribe 'avanzar' para continuar")
                x = random.randint(0,9)
                print("El número de esta sección es el:", x)
                self.codigo_caja_fuerte += str(x)
                return


    def minijuego_mano_2(self):
        print("Has entrado a un minijuego\n En esta ocasión entraras en combate con un grupo de policias")
        print("Instrucciones: Oprime la letra que aparezca en pantalla para dispararle, si te equivocas él te disparará y te quitara vida")
        print("Comencemos...")
        time.sleep(7)
        vida_oponente = 10
        while vida_oponente > 0 and self.vidas > 0:
            x = chr(random.randint(97, 122))
            print(x)
            a = input("Dispara ")
            if a == x:
                vida_oponente -= 1
                print("Le disparaste al oponentente, vidas:", "/"*vida_oponente)
            else:
                self.vidas -= 1
                print("Te dispararon, te quedan", self.vidas, "vidas")
        if self.vidas > 0:
            print("Felicidades!!!")
            print("Haz completado la prueba, escribe 'regresar' para continuar")
            print("Vidas: ", self.vidas)
            x = random.randint(0,9)
            print("El número de esta sección es el:", x)
            self.codigo_caja_fuerte += str(x)
        else:
            print("Lo siento, tus vidas se han acabado")
            self.game_over()


    def minijuego_mano_3(self):
        print("ALV!!!!(hasta la vista) atrás de ti sigue un policia vivo")
        print("Tendrás esquivar las balas para continuar a la siguiente sección")
        print("Instrucciones: Muevete al lado contrario de donde venga la bala, por ejemplo: si la bala viene a la derecha muevete a la izquierda")
        print("Teclas: \nW:Saltar\nA:Izquierda\nS:Agacharse:\nD:Derecha")
        print("Comencemos")
        i = 0
        while i < 10 and self.vidas > 0:
            x = random.randint(1, 4)
            if x == 1:
                i += 1
                movida = input("La bala viene ARRIBA ")
                movida.lower()
                if movida == 's':
                    continue
                else:
                    print('/' * self.vidas, '-->', '/' * (self.vidas - 1))
                    self.vidas -= 1
            elif x == 2:
                i += 1
                movida = input("La bala viene a la IZQUIERDA ")
                print()
                movida.lower()
                if movida == 'd':
                    continue
                else:
                    print('/' * self.vidas, '-->', '/' * (self.vidas - 1))
                    self.vidas -= 1
            elif x == 3:
                i += 1
                movida = input("La bala viene ABAJO ")
                print()
                movida.lower()
                if movida == 'w':
                    continue
                else:
                    print('/' * self.vidas, '-->', '/' * (self.vidas - 1))
                    self.vidas -= 1
            else:
                i += 1
                movida = input("La bala viene a la DERECHA ")
                print()
                movida.lower()
                if movida == 'a':
                    continue
                else:
                    print('/' * self.vidas, '-->', '/' * (self.vidas - 1))
                    self.vidas -= 1
        if self.vidas > 0:
            print("Felicidades!!!")
            print("Haz completado la prueba, escribe 'regresar' para continuar")
            x = random.randint(0,9)
            print("El número de esta sección es el:", x)
            self.codigo_caja_fuerte += str(x)
        else:
            print("Lo siento, tus vidas se han acabado")
            self.game_over()


    def minijuego_mano_4(self):
        duracion_ciclo = 60
        codigos = []
        diccionario = {'A': '1000', 'B': '1100', 'C': '1110', 'D': '1111', 'E': '0100', 'F': '0110', 'G': '0111', 'H': '0010', 'I': '0011', 'J': '0000', 'K': '1001', 'L': '1010', 'M': '0101', 'N': '0001', 'O': '1101', 'P': '1011'}
        print("ADVERTENCIA !!! \nSe te olvidó que la sección de seguriadad tiene cámaras, te vieron y se activo una bomba, tienes que desactivar la bomba en menos de 60 segundos")
        print("Instrucciones: Se te dara una secuencia de codigos, tu tendras que ver que letra le corresponde a cada código con el siguiente diccionario")

        #Imprime el diccionario
        for key, value in islice(diccionario.items(), 16):
            print(f'{key}: {value}')

        #Crea 10 codigos de 4 digitos cada uno
        for i in range(10):
            codigo = ""
            for _ in range(4):
                x = random.randint(0,1)
                codigo += str(x) 
            codigos.append(codigo)
        #La computadora mapea la palabra según los códigos anteriores y el diccionario
        aux = ""
        for i in range (10):
            for clave, valor in diccionario.items():
                if codigos[i] == valor:
                    aux += str(clave)
        """print(aux.lower())"""

        class Temporizador(threading.Thread):
            def __init__(self, duracion):
                super().__init__()
                self.duracion = duracion
                self.terminado = threading.Event()

            def run(self):
                time.sleep(self.duracion)
                self.terminado.set()

        class Lector(threading.Thread):
            def __init__(self):
                super().__init__()
                self.palabra = None
                self.detener = threading.Event()

            def run(self):
                while not self.detener.is_set() and not temporizador.terminado.is_set():
                    self.palabra = input("Escribe tu palabra: ")
                    if self.palabra.lower() == aux.lower():
                        self.detener.set()
                        temporizador.terminado.set()
                        print("FELICIDADES!!!!!\nEspera unos segundos...")

        temporizador = Temporizador(duracion_ciclo)
        lector = Lector()
        inpu = 'a'
        while inpu != 's':
            inpu = input("Para comenzar presiona la letra s\n")
            if inpu == 's':
                print(codigos)
                temporizador.start()
                lector.start()
                tiempo_inicio = time.time()

        while not temporizador.terminado.is_set():
            if lector.palabra is not None:
                if lector.palabra.lower() != aux.lower():
                    tiempo = int(duracion_ciclo - (time.time() - tiempo_inicio))
                    print("Palabra incorrecta\t Te quedan:", tiempo, "segundos")
                    lector.palabra = None

        if temporizador.terminado.is_set() and not lector.detener.is_set():
            print()
            print("Se acabó el tiempo")
            lector.detener.set()
            self.game_over()
        #OJO AQUI
        x = random.randint(0,9)
        print("El número de esta sección es el:", x)
        self.codigo_caja_fuerte += str(x)
        print("Excelente, has pasado todas las pruebas ahora solo escribe 'decifrar' para llegar a la bóveda y decifrar el código") #OJO AQUI


    def decifrar_caja_fuerte_mano(self):
        def botton_1():
            x = int(label1.cget("text")) + 1
            if x == 10:
                x = 0
            x = str(x)
            label1.config(text=x)
        def botton_2():
            x = int(label2.cget("text")) + 1
            if x == 10:
                x = 0
            x = str(x)
            label2.config(text=x)
        def botton_3():
            x = int(label3.cget("text")) + 1
            if x == 10:
                x = 0
            x = str(x)
            label3.config(text=x)
        def botton_4():
            x = int(label4.cget("text")) + 1
            if x == 10:
                x = 0
            x = str(x)
            label4.config(text=x)
        def botton_5():
            x = int(label1.cget("text"))
            if x == 0:
                x = 9
            else:
                x -= 1
            x = str(x)
            label1.config(text=x)
        def botton_6():
            x = int(label2.cget("text"))
            if x == 0:
                x = 9
            else:
                x -= 1
            x = str(x)
            label2.config(text=x)
        def botton_7():
            x = int(label3.cget("text"))
            if x == 0:
                x = 9
            else:
                x -= 1
            x = str(x)
            label3.config(text=x)
        def botton_8():
            x = int(label4.cget("text"))
            if x == 0:
                x = 9
            else:
                x -= 1
            x = str(x)
            label4.config(text=x)

        def botton_9():
            numero = ""
            numero += label1.cget("text")
            numero += label2.cget("text")
            numero += label3.cget("text")
            numero += label4.cget("text")
            if numero == self.codigo_caja_fuerte:
                print("Felicidaaaaadeeeeees!!!!!!, Lograste entrar a la caja fuerte")
                print("Fin del juego")
                ventana.destroy()
                time.sleep(3)
                self.minijuego_mano_5()
            else:
                if self.intentos_caja_fuerte > 0:
                    ventana.destroy()
                    print("Ese no es el número, te quedan", self.intentos_caja_fuerte, "más")
                    self.decifrar_caja_fuerte_mano()
                else:
                    print("Se acabaron tus intentos")
                    self.game_over()

        # Crear la ventana principal
        ventana = tk.Tk()
        ventana.title("")

        contenedor0 = tk.Frame(ventana)
        contenedor0.pack(expand=True)

        # Crear un botón
        button1 = tk.Button(contenedor0, text="^", command=botton_1)
        button1.grid(row=0, column=0, padx=25, pady=20)

        button2 = tk.Button(contenedor0, text="^", command=botton_2)
        button2.grid(row=0, column=1, padx=25, pady=20)

        button3 = tk.Button(contenedor0, text="^", command=botton_3)
        button3.grid(row=0, column=2, padx=25, pady=20)

        button4 = tk.Button(contenedor0, text="^", command=botton_4)
        button4.grid(row=0, column=3, padx=25, pady=20)


        contenedor1 = tk.Frame(ventana)
        contenedor1.pack(expand=True)

        # Crear un etiqueta
        label1 = tk.Label(contenedor1, text="0")
        label1.grid(row=0, column=0, padx=28, pady=20)

        label2 = tk.Label(contenedor1, text="0")
        label2.grid(row=0, column=1, padx=28, pady=20)

        label3 = tk.Label(contenedor1, text="0")
        label3.grid(row=0, column=2, padx=28, pady=20)

        label4 = tk.Label(contenedor1, text="0")
        label4.grid(row=0, column=3, padx=28, pady=20)

        contenedor2 = tk.Frame(ventana)
        contenedor2.pack(expand=True)

        # Crear un botón
        button5 = tk.Button(contenedor2, text="v", command=botton_5)
        button5.grid(row=0, column=0, padx=25, pady=20)

        button6 = tk.Button(contenedor2, text="v", command=botton_6)
        button6.grid(row=0, column=1, padx=25, pady=20)

        button7 = tk.Button(contenedor2, text="v", command=botton_7)
        button7.grid(row=0, column=2, padx=25, pady=20)

        button8 = tk.Button(contenedor2, text="v", command=botton_8)
        button8.grid(row=0, column=3, padx=25, pady=20)

        contenedor3 = tk.Frame(ventana)
        contenedor3.pack(expand=True)

        botton9 = tk.Button(contenedor3, text="Aceptar", command=botton_9)
        botton9.grid(row=0, column=3, padx=25, pady=20)

        # Iniciar el bucle principal de la interfaz gráfica
        ventana.mainloop()


    def minijuego_mano_5(self):
        print("AUN NO GANAS, TE HAN ATRAPADOOOO!")
        print("Para escapar escribe un número del 1 al 7, generaremos un número al azar, si coincide con el tuyo PIERDES si no coincide GANARAS")
        a = input("Escribe tu numero: ")
        x = random.randint(1, 7)
    
        if x == a:
            print("Lo siento, perdiste")
            self.game_over()
        else:
            print("Ufff, por poco pierdes, ahora si GANASTE")
            self.win()
        

    def identificacion_falsa(self):
        print("Escribe tu nombre falso:")
        self.nombre_policia = input("Nombre: ")
        print("La edad, altura y peso se te asignaran pero ten en cuenta cuales fueron esos datos asignados, puede que después los ocupes")
        print("Espera unos segundos en lo que creamos tu ID falsa")
        time.sleep(4)
        print("Listo")
        x = random.randint(28, 50)
        self.edad_policia = x
        x = random.randint(20, 99)
        self.altura_policia = (100 + x)
        x = random.randint(60, 90)
        self.peso_policia = x
        id = """
        ▓█▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓                                                           ▒░    
        ▓▓▓▓▓▓▓▒▒▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                                 
        ▓▓▓▓▓▓▓▓▓█████████████▓▓▓▓▓▓▓▓▓▓    ▒▒  ▒▒  ▓▒▒▒ ░▒▒▓▒▒ ▒▒  ▒▒▒   ▒▓ ▒▒    ▓  ▓    ▓ ▓░          
        ▓▓▓▓▓▓▓████████████████▓▓▓▓▓▓▓▓▓    ▒▒▒▒▒▒  ▒█▓▒  ▓▒▒█▒█▒█ ▓▒ ▒▓  ▒▓ ▒▒                          
        ▓▓▓▓▓▓▓█████████▓▓██████▓▓▓▓▓▓▓▓    ▒▒  ▒▓ ▒▒▒▒▒▓ ▓▒▒ ▓▒▒ ░▒▒▒▒▒  ▒▓ ▒▒    ▓ ▓▒ ▒▒ ░ ▒ ▒         
        ▓▓▓▓▓▓████▓▓▒▒▓▒▒▒░░▒▒▒██▓▓▓▓▓▓▓                                                                 
        ▓▓▓▓▓█████▓▒▒░▒▒░░░░▒▒▒▓█▓▓▓▓▓▓▓                                                                 
        ▓▓▓▓▓█████████▒░▒██████▒█▓▓▓▓▓▓▓       █▒ █▓██      █▓   █     █  ░ █ █ ▒                        
        ▓▓▓▓▓▓█▒███████▓█▓███ ░ █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   █       ▓   █ ▒  ▒                            
        ▓▓▓▓▓█████▓███▓▒▓█▓▓▓▒ ▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓░                                        
        ▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▒▒▒▒░░░░░█▓▓▓▓▓▓▓░░░░█░██░░░███████████░█████▓▓▓ █▒ █ ░                           
        ▓▓▓▓▓▓▓▓▓▓▓▓██▓▓█▒▒░░░░▓▓▓▓▓▓▓▓▓░░░░░░░░░░░█░█░░█░█░░░░█░██░▓▒▓▓▓▓▓▓  █ ██ █ █▓ █ █ █ █          
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒░░░░▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░▒░▓░░░░░██▓█░░░░░░░▓█▓▓▓▓▓▓  █ █                   
        ▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▒▒▒▒░░▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓                    
        ▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒█▒▒▒▒▒▒█░█░░░░░░ █ ░░░░░░▒░█░░░░░░░░█▓▓▓▓▓    ░           
        ▓▓▓▓▓▓▓▓█▓██▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓            
        ▓▓▓▓█▓▓▓▓▓█▓▓▓▓▓▓▒▒▒▒▒▒█▓▓▓▓▓▓▓▓    █  █     ▒█▒▒▒▓▓▓█▒▓░░░█▒▒▒ █░  ░░░░░░░██░░▒██░█░▓▓▓▓        
        █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒█▓▓▓▒▓▓▓▓▓                      ▒▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░▓▓▓▓     
        ▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▒▒░░░▓█▓▓▓▓▓▓▓▓▓█    █ ▓  █  ░ █       ░▒     ▓▒▒▒▒▒▒▒▒▒▒▒ ░░░░░░░░░░░░░░░░░░▓▓   
                                                                            ▒▒▒▓▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░   

                Nombre:      {}                                                                           
                                                                                                
                Edad:        {}                                                                     
                                                                                                            
                Altura       {}                                                                     
                
                Peso         {} 
        """.format(self.nombre_policia, self.edad_policia, self.altura_policia, self.peso_policia)
        print(id)
        print("Si ya viste tus datos escribe 'listo' para continuar")


    def checar(self):
        lista = [None]*5
        tulista = [None]*5
        num = ""
        print("Instrucciones: Son 5 cajas, si ves que la cantidad de dinero coincide con la tuya escribe 'correcto' de lo contrario escribe 'reportar'")
        a = 0
        for i in range(5):
            for j in range(6):
                x = random.randint(0,9)
                num += str(x)
            lista[i] = num
            a = random.randint(1,2)
            if (i+1) % 2 != 0 and a == 2: #CREO QUE PUDIERAMOS QUITAR LA PRIMERA CONDICION
                tulista[i] = num
            else:
                tulista[i] = str(int(num)-999)
            num = ""
        print("Lista del banco: ", lista)
        print("Tu lista:        ",tulista)
        i = 0
        while i < 5 and self.vidas > 0:
            if lista[i] == tulista[i]:
                print("Número", i+1, ":")
                resp = input()
                while resp.lower() != 'correcto' and resp.lower() != "reportar":
                    resp = input("Palabra no válida, vuelve a ingresar tu respuesta: ")
                if resp.lower() == "correcto":
                    i += 1
                else:
                    self.vidas -= 1
                    print("Incorrecto, pierdes una vida, vuelve a intentar\nVidas: ", self.vidas)
            else:
                print("Número", i+1, ":")
                resp = input()
                while resp.lower() != 'correcto' and resp.lower() != "reportar":
                    resp = input("Palabra no válida, vuelve a ingresar tu respuesta: ")
                if resp.lower() == "reportar":
                    i += 1
                else:
                    self.vidas -= 1
                    print("Incorrecto, pierdes una vida, vuelve a intentar\nVidas: ", self.vidas)

        if self.vidas == 0:
            self.game_over()
        else:
            print("Felicidades, corroboraste el dinero en las cajas, escribe 'continuar' para seguir")
            x = random.randint(0,9)
            print("El número de esta sección es el:", x)
            self.codigo_caja_fuerte += str(x)
        
    def caminar(self):
        print("Caminando...")
        time.sleep(4)
        print("Listo, para entrar a las oficinas escribe 'entrar'")
    
    def hablar(self):
        print("\t\t\t\t\t\tPolicia: Hola, como estás?")
        resp = input()

        if "tu" in resp.lower() or "usted" in resp.lower():
            print("\t\t\t\t\t\tMmm como siempre, todo bien")
        elif "bien" in resp.lower() or "excelente" in resp.lower() or "perfecto" in resp.lower() or "mas o menos" in resp.lower() or "feliz" in resp.lower() or "siempre" in resp.lower() or "genial" in resp.lower() or "normal" in resp.lower():
            print("\t\t\t\t\t\tMe da gusto")
        elif "mal" in resp.lower() or "pesimo" in resp.lower() or "cansado" in resp.lower() or "cansada" in resp.lower() or "enojado" in resp.lower() or "enojada" in resp.lower() or "aburrida" in resp.lower() or "aburrido" in resp.lower() or "flojera" in resp.lower() or "horrible" in resp.lower() or "triste" in resp.lower():
            print("\t\t\t\t\t\tBueno espero que te cambie el animo")
        print("\t\t\t\t\t\tY que haces por aqui?")
        resp = input()
        if "paseando" in resp.lower() or "caminando" in resp.lower() or "platicando" in resp.lower() or "vigilando" in resp.lower() or "checando" in resp.lower() or "hablando" in resp.lower() or "inspeccionando" in resp.lower() or "revisando" in resp.lower() or "comprobando" in resp.lower() or "corroborando" in resp.lower() or "asegurando" in resp.lower():
            print("\t\t\t\t\t\tAaaa muy bien, bueno entonces sigue con eso para que puedas salir temprano")
        elif "nada" in resp.lower():
            print("\t\t\t\t\t\tMmm que aburrido eres pero bueno, tengo cosas que hacer, nos vemos luego")
        elif "robando" in resp.lower() or "asaltando" in resp.lower() or "atracando" in resp.lower() or "infiltrado" in resp.lower() or "incognito" in resp.lower() or "sigiloso" in resp.lower():
            self.game_over()
        print("\t\t\t\t\t\tOye antes de que te vayas, quería preguntarte si tienes algo que hacer en la tarde")
        resp = input()
        if "se" in resp.lower():
            print("\t\t\t\t\t\tEs que quería ver si estabas disponible para un partido de fut en la tarde")
            resp = input()
            if "si" in resp.lower() or "va" in resp.lower() or "sale" in resp.lower():
                print("\t\t\t\t\t\tAa sale sale, entonces nos vemos en las canchas")
                resp = input()
            elif "no" in resp.lower():
                print("\t\t\t\t\t\tMmm bueno no hay problema, para la otra")
                resp = input()
        elif "si" in resp.lower():
            print("\t\t\t\t\t\tEs que era para un juego de fut pero bueno, si te desocupas me llamas si no ya nos veremos mañana")
            resp = input()
        elif "no":
            print("\t\t\t\t\t\tA que bueno, quieres ir a un partido de futbol, con unos amigos?")
            resp = input()
            if "se" in resp.lower():
                print("\t\t\t\t\t\tEsta bien, si cambias de opinión me dices para que llegues")
                resp = input()
            elif "no" in resp.lower():
                print("\t\t\t\t\t\tEsta bien, a ver si a la otra si quieres")
                resp = input()
            elif "si" in resp.lower():
                print("\t\t\t\t\t\tVa nos vemos en la noche")
                resp = input()

        print("Perfecto, terminaste de hablar con el policia y no sospecho, escribe 'seguir' para continuar")
        x = random.randint(0,9)
        print("El número de esta sección es el:", x)
        self.codigo_caja_fuerte += str(x)

    def datos(self):
        print("Tu cara se me hace desconocida, eres nuevo ?, bueno no importa, te haré unas preguntas y veré si coinciden con tu identificación")
        resp = input("Cual es tu nombre? ")
        if resp.lower() == self.nombre_policia.lower():
            print("Correcto")
        else:
            print("Eres un infiltrado")
            self.game_over()
        resp = input("Cual es tu peso? ")
        if int(resp) == self.peso_policia:
            print("Mmm bien")
        else:
            print("Eres un infiltrado")
            self.game_over()
        resp = input("Cuántos años tienes? ")
        if int(resp) == self.edad_policia:
            print("Ok, una pregunta más")
        else:
            print("Eres un infiltrado")
            self.game_over()
        resp = input("Cuánto mides? ")
        if int(resp) == self.altura_policia:
            print("Esta bien, si eres un policia")
        else:
            print("Eres un infiltrado")
            self.game_over()
        print("Muy bien, supiste responder las preguntas, escribe 'seguir' para ir a la última sección")
        x = random.randint(0,9)
        print("El número de esta sección es el:", x)
        self.codigo_caja_fuerte += str(x)
    
    def cables(self):
        print("Has llegado a seguridad... y tendras que conectar cables")
        print("Instrucciones: Tendrás que escribir la posición del número de arriba, empezando de izquierda a derecha, y después escribir la posición del número de abajo al cual lo relacionarás")
        print("Ejemplo: El cable en la posición 1 lo unirás con el cable en la posición 7 y lo tienes que escribir en este formato sino perderás : '1:7'")

        lista = [None]*5
        lista_revuelta = [None]*5
        for i in range(5):
            x = random.randint(0,9)
            lista[i] = x
        lista_revuelta = lista.copy()
        random.shuffle(lista_revuelta)

        cables = """
            {}    {}    {}    {}    {}
            █    █    █    █    █
            █    █    █    █    █
            █    █    █    █    █
            █    █    █    █    █
            █    █    █    █    █
            █    █    █    █    █
            {}    {}    {}    {}    {}
        """.format(lista[0], lista[1], lista[2], lista[3], lista[4], lista_revuelta[0], lista_revuelta[1], lista_revuelta[2], lista_revuelta[3], lista_revuelta[4])

        aux = ""
        intentos = 2
        i = 0

        while i < 5:
            print(cables)
            aux = ""
            x = lista_revuelta.index(lista[i]) + 1
            aux += str(i+1) + ":" + str(x)
            #print(aux)
            print("Ingresa tu respuesta, vamos con el cable: ", i+1)
            resp = input()
            if int(resp[0:1]) != i and (resp == aux or lista[int(resp[0:1])-1] == lista_revuelta[int(resp[2:])-1]):
                print("Muy bien")
                i += 1
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                intentos -= 1
                print("Incorrecto, vuelve a intentarlo\nTe quedan:", intentos, "intentos")
            if intentos == 0:
                self.vidas -= 1
                intentos = 2
                if self.vidas > 0:
                    print("Perdiste una vida, vuelve a intentarlo", "\nVidas:", self.vidas)
                else:
                    print("Se te acabaron tus vidas")
                    self.game_over()
        x = random.randint(0,9)
        print("El número de esta sección es el:", x)
        self.codigo_caja_fuerte += str(x)
        print("Escribe 'decifrar' para poner el código en la caja fuerte")

    
        
    def minh1(self):
        diccionario = """ 
                                        a b c d e f g h i j k l m n o p q r s t u v w x y z
                                        ! @ # $ % ^ & * ( ) - _ + = [ ] { } | \ / ? < > , . """
        
        
        print("Para poder conseguir entrar a la base de datos del banco, necesitas conseguir la contraseña de la computadora")
        print("\t la contrseña esta en un cifrado por lo que sera necesario conseguir la contraeña para despues poderla decifrar")
        print("\t te hemos brindado un dicionario que te puede ayudar, ya que con este vamos a poder descifrar la contrseña ")
        print("Ojo, este solo te dara una parte de la contraseña vas a necesitar hacermas para conseguirla, asi que aprendetela")
        print("\n",diccionario)
        
        
        print("Contraseña: = [ |    * ! } ( !     % _")
            #  c o n t r a s e ñ a:    n o s    h a r i a     e l 
        while True:
            cont = input()
            if 'nos haria el' in cont:
                print("HAS ENCONTRADO UNA PARTE DE LA CONTRSEÑAA")
                print("Da en seguir")
                return False
            else:
                print("Intenta de nuevo")
                vidas -= 1



    def jugar_adivinanza(self):
        palabras = ['python', 'juego', 'adivinanza', 'palabra', 'decifrar']
        palabra = random.choice(palabras)
        adivinanza = ['_'] * len(palabra)
        intentos = 13
        vidas = 3

        print("¡Bienvenido al juego de adivinanzas!")
        print("Tienes que adivinar la palabra. La palabra tiene", len(palabra), "letras.")
        print(" ".join(adivinanza))
        print("\n")

        while vidas > 0:
            while intentos > 0 and '_' in adivinanza:
                letra = input("Ingresa una letra: ")
                if letra in palabra:
                    for i in range(len(palabra)):
                        if palabra[i] == letra:
                            adivinanza[i] = letra
                    print("¡Correcto!")
                else:
                    intentos -= 1
                    print("Incorrecto. Te quedan", intentos, "intentos.")
                print(" ".join(adivinanza))
                print("\n")

            if '_' in adivinanza:
                vidas -= 1
                if vidas == 0:
                    print("Te has quedado sin vidas.")
                    return False
            else:
                print("¡Felicidades, has ganado!")
                print("La otra parte de la contraseña es: favor de")
                print("Presiona la tecla R para continuar")
                return True

    def minh2(self):
        for i in range(3):
            ganado = self.jugar_adivinanza()
            if ganado:
                break

        if not ganado:
            print("Lo siento, has perdido. Fin del juego.")
            



    def minh3(self):
        numero_a_adivinar = random.randint(1, 100)
        numero_codificado = base64.b64encode(str(numero_a_adivinar).encode())

        print("Es un numero de 0 a 100")
        print(f"El número codificado es: {numero_codificado.decode()}")

        while True:
            entrada_usuario = input("Decodifica el número: ")

            if not entrada_usuario.isdigit():
                
                print("Por favor, introduce un número válido.")
                continue

            numero_usuario = int(entrada_usuario)

            if numero_usuario == numero_a_adivinar:
                print("¡Felicidades! Has decodificado el número correctamente.")
                print("La otra parte de la contraseña es: 'de'")
                print("Presiona M para continuar")
                break
            elif numero_usuario < numero_a_adivinar:
                print("El número es mayor. Intenta de nuevo.")
            else:
                print("El número es menor. Intenta de nuevo.")


    def generar_codigo(self):
        digitos = [str(num) for num in range(1, 7)]
        random.shuffle(digitos)
        """print(digitos[:4])"""
        return ''.join(digitos[:4])

    def obtener_entrada(self):
        return input("Ingresa tu número: ")

    def dar_pistas(self, codigo, entrada_usuario):
        if codigo == entrada_usuario:
            return "¡Has ganado!"

        pistas = []

        for ind, digito in enumerate(entrada_usuario):
            if digito == codigo[ind]:
                pistas.append("Manuel")
            elif digito in codigo:
                pistas.append("Memo")
        if not pistas:
            return "Rodri"

        pistas.sort()
        return " ".join(pistas)

    def minh4(self):
        print("\n¡Vamos a jugar Memo, Rodri y Manuel!")
        print("\tLas reglas son sencillas, se asignara un codigo de 4 digitos, cada digito puede ser un numero del 1 al 6, lo que tu tines que hacer")
        print("\tes adivinar el codigo, para eso tienes 10 intentos, cada vez que ingreses un numero, te daremos pistas, si el numero que ingresaste ")
        print("\testa en el codigo te diremos 'Memo', si el numero que ingresaste esta en el codigo y esta en la posicion correcta te diremos 'Manuel',\n y te diremos 'Rodri' si el numero que ingresaste no esta en el codigo")
        codigo_secreto = self.generar_codigo()
        print("He generado un número.")

        while True:
            entrada_usuario = self.obtener_entrada()
            resultado = self.dar_pistas(codigo_secreto, entrada_usuario)
            print(resultado)

            if resultado == "¡Has ganado!":
                print("La ultima parte de tu contraseña es: 'excentar?'")
                print("Es momento de de poner la contraseña, pero no es como piensas, la contraseña es la respuesta a la pregunta")
                break

 
nom = input("Ingresa tu nombre: ")
print("Cargando...")
time.sleep(2) 
os.system('cls' if os.name == 'nt' else 'clear')
juego = Juego(nom)
juego.jugar()
