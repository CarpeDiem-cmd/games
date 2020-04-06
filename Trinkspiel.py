import random
import os
import textwrap
import time
import sys

screen_width = 100

"""
leading screen = if player x leads by 5 and 10 points print("you are leading / you are even more leading")

TO DO list:
*1d30 für Bonusaufgabe





"""


themen =   ["EXTREM!", "Wahrheit", "Pflicht", "Schlücke verteilen", "Ich habe noch nie", "Would you rather", "Sport", "Schauspiel"]
moeglichkeiten = [
  #EXTREM!                                                                           
  [
    "MASS CHALLENGE! Begieb dich auf einen Stuhl in die Mitte des Raumes und füll deinen Mund bis zum Anschlag mit Wasser. Jeder Spieler hat nun jeweils 30\" Zeit dich zum Lachen zu bringen.Wenn du lachst trinkst du 1 Schluck. Wenn du nicht lachst trinkt er 2 Schluck.",#3 point
    "Versuch dich an einem Kopf oder Handstand oder trink 5 Schluck.", #3 point
    "15 Klimmzüge. Lass dir Zeit. Falls die du wieder dran und noch nicht fertig bist, bist trink 10 Schluck",#4 points
    "Jeder Spieler stellt dir eine Allgemeinwissenfrage. Trink 3 Schluck wenn du etwas nicht weißt.", #4 points
    "Bis zur nächsten Runde wirst du mit zwei Pingpongbällen beworfen. Trink 2 Schluck für jeden Ball der trifft (5sec cooldown/Wurf und 5sec Pause nach jedem Schluck)", #5 point
    "Russisches Roulette. Schließ die Augen. Ein Spieler hält einen Pingpongball hinter dem Rücken. Trink 20 Schlücke wenn du ihn erwischt. Ein anderer Spieler hält einen Pingpontschläger hinter dem Rücken. Alle anderen trinken 2 Schlücke wenn du ihn erwischst.", #5 points
    "Trink 3 Runden lang die doppelte Menge an Schlücke.",
    "Verbring die nächsten 3 Runden am Sportgerät in der Sitzposition mit ausgestreckten Beinen. Trink jedes mal 2 Schluck wenn die Beine runter kommen.",
  ],
  #wahrheit
  [
    "Trink 2 Schlücke, wenn du es dir schon einmal verkniffen hast, nachts aufs Klo zu gehen, weil du am Abend einen Horrorfilm gesehen hast.",
    "Trink 3 Schlücke, wenn du dir schon einmal Geld geliehen hast, ohne es zurückzuzahlen.",
    "Verrate uns deinen Celebrity Crush oder trink 3 Schlücke.",
    "Wie alt warst du bei deinem ersten Mal? Trink 2 Schlücke, wenn du minderjährig warst.",
    "Trink 3 Schlücke, wenn du unter der Dusche pinkelst.",
    "Trink 3 Schlücke, wenn du schon einmal etwas gestohlen hast.",
    "Warum magst du das Geburtstagskind? Du und das Geburtstagskind stoßen an und trinken jeweils einen Schluck.",
    "Jeder Spieler kann dir eine persöhnliche Frage stellen. Trink jeweils 2 Schluck wenn du sie nicht beantwortest.",
  ],
  #pflicht
  [
    "Sing ein Lied von Sido. Die Person rechts von dir entscheidet, ob du gut genug gesungen hast oder 2 Schlücke trinken solltest.",
    "Zieh dein T-shirt verkehrt herum an oder trink 4 Schlücke",
    "Zieh ein Kleidungsstück aus oder trink 3 Schlücke",
    "Sing ein Lied mit vollem Mund. Wer das Lied erkennt verteilt 4 Schlücke an die anderen Spieler.",
    "Mach eine berühmte Persönlichkeit nach. Wer sie erkennt verteilt 4 Schlücke andie anderen Spieler.",
    "Lese deine letzte versendete Nachricht laut vor (oder trink 3 Schlücke).",
    "Erzähl einen Witz. Wenn niemand lacht, trink 2 Schlücke und schäm dich.",
    "Mach Lukas seinen nächsten Drink. Kein aber und keine Trink x Schluck Clausel.",
  ],
  #Schlücke_verteilen 
  [
    "Verteil so viele Schlücke, wie es Leute an diesem Tisch gibt, die sich immer wieder zum Affen machen würden.",
    "Verteil 3 Schlücke an einen Spieler, der brauner ist als du, wenn möglich Ansonsten trink sie selbst.",
    "Verteile 5 Schlücke an den Lahmarsch, der die meisten Aufgaben umgeht indem er immer die 'oder trink x Schluck' Option wählt.",
    "Verteil 5 Schlücke, wenn du schon einmal Kondome mit Geschmack benutzt hast. Ansonsten trink sie selbst.",
    "Entscheide, wer hier den schönsten Mund hat. Sie/Er/D trinkt 3 Schlücke.",
    "Verteile denjenigen, die heute am meisten die Klappe offen hatte 5 Schlücke.",
    "Das Geburtstagskind trinkt 5 Schlücke oder verteilt sie, du entscheidest.",
    "Erzähle zwei Wahrheiten und eine Lüge aus deinem Leben. Wer falsch liegt trinkt 3 Schlücke.",
  ],
  #noch_nie
  [ 
    "Ich hab noch nie illegale Drogen (außer Cannabis) genommen (1 Schluck).",
    "Ich hab noch nie jemanden geküsst und es danach bereut (1 Schluck).",
    "Ich hab noch nie jemanden entjungfert (2 Schluck).",
    "Ich hab noch nie jemanden beim Sex erwischt (2 Schluck).",
    "Ich hab noch nie Probleme mit der Polizei gehabt (2 Schluck).",
    "Ich hab noch nie bei einer Prüfung gemogelt(3 Schluck).", 
    "Ich hab noch nie etwas im Internet bestellt, weil ich mich nicht getraut habe, es im Laden zu kaufen(1 Schluck).",
    "Ich hab noch nie meinen Haustürschlüssel verloren. (1 Schluck)",                                                                     
  ],
  #would_you_rather
  [
    "Würdest du lieber die Art oder den Zeitpunkt deines Todes wissen? (das Wissen verhindert nicht deinen Tod)",
    "Würdest du lieber einen Partner mit diametralen politischen oder religiösen Meinungen haben",
    "Würdest du lieber fliegen oder gedanken lesen können? (ohne wissenschaftliche Logik)",
    "Wärst du lieber halb so groß oder doppelt so schwer? (Fettgebewe obviously)",
    "Würdest du einmal russisches Roulette mit einer Kugel für 1 Million€ spielen?",
    "Katzen oder Hunde?",
    "Team Edward oder Team Jacob?",
    "Würdest du den Tod von 100 Unbekannten, dem Tod eines geliebten Menschen vorziehen?",
  ],
  #Sport
  [
    "Mach 20 Squats oder trink 3 Schlücke.",
    "Hänge eine Minute an der Klimmzugstange oder 2 Schlücke trinken. Wenn du noch hängst, wenn du wieder dran bist, kannst du 10 Schlücke verteilen (max 4/Person)", 
    "Dreh dich 30x im Kreis oder 3 Schlücke trinken (Aufpassen bitte).",
    "Renne auf der Stelle bis deine Runde wieder anfängt oder 2 Schlücke trinken.", 
    "Schlag 20x mit voller Wucht in die Luft und sag jedes mal 'HAI' oder trink 3 Schluck.", 
    "Such dir einen Partner der dich anschreit, während du 10x Liegestütze machst oder 2 Schluck trinken.", 
    "Such dir einen Partner mit dem du um drei Punkte im Ping Pong spielst. Verlierer muss 3 Schluck trinken.",
    "MASS CHALLENGE! Jeder am Tisch gibt dir eine einzige Aufgabe (Z.B.:EINE Liegestütze) oder trinke 5 Schluck!",
  ], 
  #Schauspiel
  [
    "Schnapp dir den Spieler rechts von dir und stelle mit ihm eine extrem ernste 80 Jahre KongFU Scene nach, bei der du deinen Vater rächst. Wenn einer von euch lacht muss er 1 Schluck trinken.",
    "Mach einen anderen Spieler nach. Wenn dieser 1 Schluck trinkt bevor man ihn errät, muss du 3 Schluck trinken. Sonst muss er selber 3 Schluck trinken.", 
    "Du bist jetzt der Klatsch Mann/die Klatsch Frau - wenn du es schaffst bis zum Ende des Spiels 3 verschiedenen Leuten sanft und liebevoll (und nicht) auf den Nacken zu klatschen, müssen die 3 Geklatschten 4 Schluck trinken.",
    "Mach einen greisen alten Mann nach. Die anderen entscheidet wie gut du warst (super!-scheiße!) und basiert darauf deine Schlücke (von 0-5)", 
    "MASS CHALLEGNE! Schnapp dir die Spieler links und rechts neben dir. Der Spieler mit den meisten Punkten nach euch entscheidet welche Scene ihr völlig übertrieben zu dritt schauspielern müsst. Wenn ihr keinen zum Lachen bringt, müsst ihr alle 3 Schlücke trinken.", 
    "Benutze den Körper des Spielers links von dir um 'Freude schöner Götterfunkenzu spielen. Dein Mitspieler trinkt 1 Schluck. ", 
    "Du bist von jetzt an Mr./Mrs. Unbeeindruckt. Egal was passiert Du bist extrem unbeeindruckt. (3 Runden lang oder trink 5 Schluck)",
    "Sitz drei Runden lang auf dem Boden und sag nur 'GRLM GRLM' wenn du angesprochen wirst.",
  ], 
]

debug = False
player_stats = dict()

def roll():
  return random.randint(1,8)

def initialize():
  global player_stats
  global debug
  #rank: global offense against real programmers

  spieler_anzahl = 2
  if not debug:
    spieler_anzahl = int(input("Wie viele Spieler?\n")) 
 
  print("{} Spieler.".format(spieler_anzahl))
  
  #initialize stats with player names and 0 points each
  for i in range(spieler_anzahl): 
    name = ""
    if debug:
      list_of_prepared_names_because_lazy = ["cami", "luki"]
      name = list_of_prepared_names_because_lazy[i] # array[i] = select i-th thing from array
    else:
      name = input("Name für Spieler #{}?\n".format(i+1)) 
    player_stats[name] = 0
  
  print(player_stats) 
  input("Drücke ENTER um zu beginnen")
  os.system('cls')
  main_game_loop()
  #k, now we need to increment it every new "cycle"tg
  #print("entire dict:", player_stats) # prints entire dict
  
def main_game_loop():
  global topic_number
  global points
  global name
  for name in player_stats:
    points = player_stats[name] 
    print(player_stats)   
    print("Spieler am Zug: {} Punkte: {}".format(name, points)) 
    print("Thema wird gewürfelt")              
    input("Drücke ENTER um zu würfeln")

    rnumber = roll() # roll the die
    topic_number = rnumber-1 # subtract 1 from the dice because array indices
    topic = themen[topic_number] # get the name of the topic.

    print("[{}] -> {}".format(rnumber, topic))
    if rnumber == 1:
      eingabe = input("Du hast EXTREM gewürfelt. EXTREM Aufgaben geben viele Punkte, sind aber schwererMöchtest du einmal neu würfeln?  j/n\n")
      if eingabe.lower() in ["j", "ja", "jep", "jeps", "sicher", "si"]:
        rnumber_extreme = roll()
        topic_number = rnumber_extreme-1
        topic = themen[topic_number]
        print("[{}] -> {}".format(rnumber_extreme, topic))
      elif eingabe.lower() not in ["j", "ja", "jep", "jeps", "sicher", "si"]:
        pass
      #elif eingabe.lower() in ["n", "nein", "nope", "niet", "no"]:
        #roll_aufgaben() 
    else:
      pass
    input("Drücke ENTER um deine Aufgabe zu würfeln")
    rnumber = roll() 
    aufgabe_number = rnumber-1
    
    aufgabe = moeglichkeiten[topic_number][aufgabe_number]  
    print("[{}] -> {}\n".format(rnumber, aufgabe))
    input("\n\n\n\n\n\n\n\n\nDrücke Enter wenn alle bereit sind")
    if topic_number == 0:
      if aufgabe_number in [0, 1]: 
        player_stats[name] = points+2
      elif aufgabe_number in [2, 3]: 
        player_stats[name] = points+3
      elif aufgabe_number in [4, 5]:
        player_stats[name] = points+4
      elif aufgabe_number in [6, 7]:
        player_stats[name] = points+1
    else:
      player_stats[name] = points+1

    if topic_number == 0:
        if aufgabe_number in [0, 1]: 
          player_stats[name] = points+2
        elif aufgabe_number in [2, 3]: 
          player_stats[name] = points+3
        elif aufgabe_number in [4, 5]:
          player_stats[name] = points+4
        elif aufgabe_number in [6, 7]:
          player_stats[name] = points+1
    else:
        player_stats[name] = points+1
    
    if points > 14:
      print(f"{name} ist in Führung!")

    if points > 24:
      print(f"{name} hat bald gewonnen!")
  
    if points > 29:
      end_of_game()
    os.system('cls')

    #Rolls for BONUSROUND
    rnumber = random.randint(1,30)
    if rnumber > 29:
      bonus0 = "BONUSRUNDE "
      bonus1 = "- du darfst erneut würfeln"
      for character in bonus0:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.18)
      for character in bonus1:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.09)
      points = player_stats[name] 
      os.system('cls')
      print(player_stats)   
      print("BONUSRUNDE! Spieler: {} Punkte: {}".format(name, points)) 
      print("Thema wird gewürfelt")              
      input("Drücke ENTER um zu würfeln")

      rnumber = roll() # roll the again
      topic_number = rnumber-1 # subtract 1 again
      topic = themen[topic_number] # get the name of the topic, again

      print("BONUS[{}] -> {}".format(rnumber, topic))
      if rnumber == 1:
        eingabe = input("Du hast EXTREM gewürfelt. EXTREM Aufgaben geben viele Punkte, sind aber schwererMöchtest du einmal neu würfeln?  j/n\n")
        if eingabe.lower() in ["j", "ja", "jep", "jeps", "sicher", "si"]:
          rnumber_extreme = roll()
          topic_number = rnumber_extreme-1
          topic = themen[topic_number]
          print("BONUS[{}] -> {}".format(rnumber_extreme, topic))
        elif eingabe.lower() not in ["j", "ja", "jep", "jeps", "sicher", "si"]:
          pass
        #elif eingabe.lower() in ["n", "nein", "nope", "niet", "no"]:
          #roll_aufgaben() 
      else:
        pass
      input("Drücke ENTER um deine Bonusaufgabe zu würfeln")
      rnumber = roll() 
      aufgabe_number = rnumber-1
      
      aufgabe = moeglichkeiten[topic_number][aufgabe_number]  
      print("[{}] -> {}\n".format(rnumber, aufgabe))
      input("\n\n\n\n\n\n\n\n\nDrücke Enter wenn alle bereit sind")
      os.system('cls')   
      if topic_number == 0:
        if aufgabe_number in [0, 1]: 
          player_stats[name] = points+2
        elif aufgabe_number in [2, 3]: 
          player_stats[name] = points+3
        elif aufgabe_number in [4, 5]:
          player_stats[name] = points+4
        elif aufgabe_number in [6, 7]:
          player_stats[name] = points+1
      else:
        player_stats[name] = points+1
    print("================================================================================")
    
  main_game_loop()

def end_of_game():
  print(f"Glückwünsche {name} hat als erste/r {points} Punkte erreicht.\n")
  print("================================================================================")
# for character in end1:
#      sys.stdout.write(character)
#     sys.stdout.flush()
#    time.sleep(0.05)
  input()
  sys.exit()

initialize() # sets number of players, names, etc