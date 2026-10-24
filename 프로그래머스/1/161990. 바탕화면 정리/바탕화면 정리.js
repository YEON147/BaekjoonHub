function solution(wallpaper) {
    const N = wallpaper.length;
    const M = wallpaper[0].length;

    const reversed = [...wallpaper[0]].map((_, j) =>
        wallpaper.map(row => row[j]).join('')
    );

    function findStart(arr) {
        for (let i = 0; i < arr.length; i++) {
            if (arr[i].includes('#')) {
                return i;
            }
        }
    }

    function findEnd(arr) {
        for (let i = arr.length - 1; i >= 0; i--) {
            if (arr[i].includes('#')) {
                return i + 1;
            }
        }
    }

    const startLo = findStart(wallpaper);
    const endLo = findEnd(wallpaper);
    const startCol = findStart(reversed);
    const endCol = findEnd(reversed);

    return [startLo, startCol, endLo, endCol];
}