class Solution {
    /**
     * @param {number[]} asteroids
     * @return {number[]}
     */
    asteroidCollision(asteroids) {
        const stack = [];

        for (const num of asteroids) {
            let mort = false;

            while (stack.length > 0 && stack[stack.length - 1] > 0 && num < 0) {
                const top = stack[stack.length - 1];

                if (top + num === 0) {
                    stack.pop();
                    mort = true;
                    break;
                }
                if (top < Math.abs(num)) {
                    stack.pop();
                    continue;
                }
                mort = true;
                break;
            }
            if (!mort) {
                stack.push(num);
            }
        }
        return stack;
    }
}
