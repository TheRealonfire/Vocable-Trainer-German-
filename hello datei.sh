
echo "Willkommen zum Spiel"
echo "Sie sind in einer Gefängnisinsel Gefangen"
echo "Dort sehen sie zwei Dinge. Ein Stein & Ein Seil. Wähle 1 oder 2 für deinen Gegenstand"

read Gegenstand



if ["$Gegenstand" == "1"]; then

    echo "Was möchtest du machen"

    echo "1. Den Stein an die Wand werfen"

    echo "2. Den Stein an die Tür werfen"

    read a1

    if ["$a1" == "1"]; then
        echo "Der Stein Zerbricht und du verbleibst bis zu deinem Tod im Kerker :("
    else
        echo "Das Schloss geht auf und dein Stein zerbricht"
        echo "wo gehst du hin links oder rechts"
        read direction
        if [ "$direction" == "links" ]; then
            echo "Du gehst nach links und triffst auf eine Wache"
            echo "möchtest du mit ihm sprechen oder Prügeln?"
            read a2

            if [ "$a2" = "sprechen" ]; then
                echo "Der Wärter gibt dir einen Generalschluessel. Und du fliehst mit damit mit einem Boot der Wärter von der Insel"
            else
                echo "Du gehst knockout nachdem er sein Schlagstock nutzt. Game Over!"



        else
            echo "Du gehst nach rechts und fällst in einem loch, da die Bauarbeiten in dem Abteil noch nicht beendet waren"
            echo "Du bist tod, Game over!"

else
    echo "Du nimmst das seil"
    echo "Du hast zwei Möglichkeiten"
    echo "1. Du kletterst aus dem Fenster mit dem Seil"
    echo "2. Du bindest einen Knoten um das Schloß und ziehst daran"

    read a3

    if ["$a3" == "1"]; then
        echo "Das Seil reist auf dem Weg nach unten und du brichst dir das Genick. Game Over!"
    else
        echo "Du ziehst ausversehen mit dem Seil die ganze Tür ab. Die Wachen werden alarmiert"
        echo "rennst du nach links oder rechts?"
        read d2
        if ["$d2" == "links"]; then
            echo "Du gehst nach links und triffst auf eine Wachepatrollie, die dich festnimmt. Game Over!"
        else
            echo "Du gehst nach rechts und triffst auf ein loch, da die Bauarbeiten in dem Abteil noch nicht beendet. Dort Seilst du dich ab"
            echo "DU landest in einem Wäschewagon und siehst eine offene Tür."
            echo "Du hast zwei Möglichkeiten."
            echo "1. Du kannst aus dem Wäschewagon aussteigen und zur Tür rennen."
            echo "2. Du verbleibst im Wäschewagon."
            read d3
            if ["$d3" == "2"]; then
                echo "Du verbliebst Stunden im Wagon und wurdest von der Insel geschafft, da die Wäsche zum austauschen verschifft werden sollte"
            else
                echo "Du ranntest zur Tür und versuchtest einen Helikopter zu klauen aber hast zu spät gemerkt das du ihn nicht tarten konntest und du wurdest geschnappt"
fi