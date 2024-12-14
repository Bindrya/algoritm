public class TaskScheduler {
    public int leastInterval(char[] tasks, int n) {
        int[] taskCount = new int[26];
        for (char task : tasks) {
            taskCount[task - 'A']++;
        }

        int maxFrequency = 0;
        for (int count : taskCount) {
            maxFrequency = Math.max(maxFrequency, count);
        }

        int maxCount = 0;
        for (int count : taskCount) {
            if (count == maxFrequency) {
                maxCount++;
            }
        }

        int minIntervals = (maxFrequency - 1) * (n + 1) + maxCount;
        return Math.max(minIntervals, tasks.length);
    }

    public static void main(String[] args) {
        TaskScheduler scheduler = new TaskScheduler();

        char[] tasks1 = {'A', 'A', 'A', 'B', 'B', 'B'};
        int n1 = 2;
        System.out.println(scheduler.leastInterval(tasks1, n1));

        char[] tasks2 = {'A', 'C', 'A', 'B', 'D', 'B'};
        int n2 = 1;
        System.out.println(scheduler.leastInterval(tasks2, n2));

        char[] tasks3 = {'A', 'A', 'A', 'B', 'B', 'B'};
        int n3 = 3;
        System.out.println(scheduler.leastInterval(tasks3, n3));
    }
}
