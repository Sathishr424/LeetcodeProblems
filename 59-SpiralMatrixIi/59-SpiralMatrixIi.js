// Last updated: 12/6/2025, 5:54:18 am
/**
 * @param {number} n
 * @return {number[][]}
 */
var generateMatrix = function(n) {
    if (n==0) return [];
    if (n==1) return [[1]];
	var ret=new Array(n).fill(0).map(()=> new Array(n).fill(0));
	var dir = 'x+'
	var x=0,y=0;
	var xp=1,xm=0,yp=0,ym=0;
	for (var i=0; i<n*n; i++){
		ret[y][x] = i+1;
		if (dir == 'x+'){
			if (x+1 >= n || ret[y][x+1] != 0){
				dir = 'y+';
				y++;
				if (y >= n) break;
			}
			else x++;
		}else if (dir == 'y+'){
			if (y+1 >= n || ret[y+1][x] != 0){
				dir = 'x-';
				x--;
				if (x < 0) break;
			}
			else y++;
		}else if (dir == 'x-'){
			if (x-1 < 0 || ret[y][x-1] != 0){
				dir = 'y-';
				y--;
				if (y < 0) break;
			}
			else x--;
		}else if (dir == 'y-'){
			if (y-1 < 0 || ret[y-1][x] != 0){
				dir = 'x+';
				x++;
				if (x >= n) break;
			}
			else y--;
		}
	}
	return ret;
};