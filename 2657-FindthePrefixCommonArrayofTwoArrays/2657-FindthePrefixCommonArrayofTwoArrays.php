// Last updated: 17/11/2025, 9:29:54 pm
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function minimumPushes($word) {
        $n = strlen($word);

        $rem = $n % 8;
        $cnt = floor($n / 8);
        return floor($cnt * ($cnt + 1) / 2) * 8 + floor($rem * ($cnt + 1));
    }
}