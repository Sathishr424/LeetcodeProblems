// Last updated: 17/11/2025, 9:18:12 pm
class Solution {
    /**
     * @param Integer[] $A
     * @param Integer[] $B
     * @return Integer[]
     */
    function findThePrefixCommonArray($A, $B) {
        $ret = [];

        $n = count($A);
        $a = [];
        $b = [];

        for ($i=0; $i<$n; $i++) {
            $a[$A[$i]] = 1;
            $b[$B[$i]] = 1;

            $cnt = 0;
            foreach ($a as $num => $_) {
                if (isset($b[$num])) $cnt++;
            }
            $ret[] = $cnt;
        }

        return $ret;
    }
}