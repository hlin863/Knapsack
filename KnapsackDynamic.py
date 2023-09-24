import unittest


class Resource:
    def __init__(self, name, value, weight, volume):
        self.Name = name
        self.Value = value
        self.Weight = weight
        self.Volume = volume


def knapsack_dynamic_programming(items, W, V):
    factor = 100  # discretization factor
    W_discrete = int(W * factor)
    V_discrete = int(V * factor)

    n = len(items)
    K = [[[0 for _ in range(V_discrete + 1)]
          for _ in range(W_discrete + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(W_discrete + 1):
            for v in range(V_discrete + 1):
                if i == 0 or w == 0 or v == 0:
                    K[i][w][v] = 0
                elif int(items[i-1].Weight * factor) <= w and int(items[i-1].Volume * factor) <= v:
                    K[i][w][v] = max(items[i-1].Value + K[i-1][w - int(
                        items[i-1].Weight * factor)][v - int(items[i-1].Volume * factor)], K[i-1][w][v])
                else:
                    K[i][w][v] = K[i-1][w][v]

    # Backtrack to find items
    res = K[n][W_discrete][V_discrete]
    w, v = W_discrete, V_discrete
    items_in_knapsack = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res != K[i-1][w][v]:
            items_in_knapsack.append(items[i-1])
            res -= items[i-1].Value
            w -= int(items[i-1].Weight * factor)
            v -= int(items[i-1].Volume * factor)

    return K[n][W_discrete][V_discrete], items_in_knapsack


class KnapsackTests(unittest.TestCase):
    def test_example(self):
        items = [
            Resource("A", 60, 10, 0),
            Resource("B", 100, 20, 0),
            Resource("C", 120, 30, 0)
        ]
        # items = [
        #     Resource("Flour", 1680, 0.265, .41),
        #     Resource("Butter", 1440, 0.5, .13),
        #     Resource("Sugar", 1840, 0.441, .29)
        # ]
        maxWeight = 50
        maxValue, chosenItems = knapsack_dynamic_programming(items, maxWeight)
        # sort the chosen items by name
        chosenItems.sort(key=lambda item: item.Name)

        self.assertEqual(maxValue, 220)
        self.assertEqual([item.Name for item in chosenItems], ["B", "C"])


items = [
    Resource("Flour", 1680, 0.265, 0.41),
    Resource("Butter", 1440, 0.5, 0.13),
    Resource("Sugar", 1840, 0.441, 0.29)
]

maxWeight = 10
maxVolume = 4
maxValue, chosenItems = knapsack_dynamic_programming(
    items, maxWeight, maxVolume)

print(maxValue)
# if __name__ == '__main__':
#     unittest.main()
# Test with items that have the same value, weight, and volume


class UnitTest(unittest.TestCase):
    def test_same_value_weight_volume(self):
        items = [
            Resource("A", 100, 10, 0),
            Resource("B", 100, 10, 0),
            Resource("C", 100, 10, 0)
        ]
        maxWeight = 50
        maxValue, chosenItems = knapsack_dynamic_programming(items, maxWeight)
        chosenItems.sort(key=lambda item: item.Name)

        # produce debugging messages
        # print(maxValue)
        print([item.Name for item in chosenItems])

        self.assertEqual(maxValue, 200)
        self.assertEqual([item.Name for item in chosenItems], ["A", "B"])


if __name__ == '__main__':
    unittest.main()
