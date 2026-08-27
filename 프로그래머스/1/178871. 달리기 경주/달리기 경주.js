function solution(players, callings) {
    const rank = new Map();

    players.forEach((player, i) => {
        rank.set(player, i);
    });

    for (const player of callings) {
        const i = rank.get(player);
        const front = players[i - 1];

        [players[i - 1], players[i]] = [players[i], players[i - 1]];

        rank.set(player, i - 1);
        rank.set(front, i);
    }

    return players;
}