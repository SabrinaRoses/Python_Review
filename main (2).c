
int main()
{
    int horaC, minutosC, horaP, minutosP;
    float tempo, preco;

    printf("Digite a hora de chegada.\n");
    scanf("%d %d", &horaC, &minutosC);

    printf("Digite a hora de partida.\n");
    scanf("%d %d", &horaP, &minutosP);

    if(horaP == horaC && minutosC == minutosP) // se o periodo for exatamente de 24 horas, ou a hora de partida e chegada forem a mesma.
    {
        tempo = 24;
        printf("O valor a pagar por %.f horas: R$ %.2f\n", tempo, tempo*=2);
    }
    else if(horaC > horaP)// se a hora de chegada for maior que hora de partida
    {
        tempo = (24 - horaC) + horaP; // Pega quantas horas falta para completar um dia a partir da hora de chegada, e soma com a hora de partida, obtendo o total.

            if(minutosC + minutosP != 0)
            {
                tempo++; // arrendonda para cima em 1 hora ao tempo, se a soma de minutos é maior que zero.
            }

        if(tempo > 0 && tempo <= 2)
        {
            printf("O valor a pagar por %.f horas: R$ %.2f\n", tempo, preco = tempo);
        }
        else if(tempo > 2 && tempo <= 4)
        {
            printf("O valor a pagar por %.f horas: R$ %2.f\n", tempo, preco = tempo * 1.40);
        }
        else
        {
            printf("O valor a pagar por %.f horas: R$ %.2f\n", tempo, preco = tempo * 2);
        }
    }
    else // se hora de partida é maior que hora de chegada.
    {
        tempo = horaP - horaC;

            if(minutosC + minutosP != 0)
            {
                tempo++; // arrendonda para cima em 1 hora ao tempo, se a soma de minutos é maior que zero.
            }

        if(tempo > 0 && tempo <= 2)
        {
            printf("O valor a pagar por %.f horas: R$ %.2f\n", tempo, preco = tempo);
        }
        else if(tempo > 2 && tempo <= 4)
        {
            printf("O valor a pagar por %.f horas: R$ %2.f\n", tempo, preco = tempo * 1.40);
        }
        else
        {
            printf("O valor a pagar por %.f horas: R$ %.2f\n", tempo, preco = tempo * 2);
        }
    }

    return 0;
}
