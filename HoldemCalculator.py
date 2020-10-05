class HoldemCalculator:

    def __init__(self):
        self.m_MonteCarloThreshhold = 20000000

    def Calculate(self, hands, board, dead, trialCount, outResults):
        self.PreCalculate(hands, board, dead, trialCount, outResults);

        if EstimatePossibleOutcomes() > m_MonteCarloThreshhol
            CalculateMonteCarlo()
        else
            CalculateExhaustive()

        return PostCalculate()

    def CalculateMC(self, hands, board, dead, numberOfTrials, results):
        pass

    def CalculateEE(self, hands, board, dead, results):
        pass

    def PreCalculate(self, hands, board, dead, numberOfTrials, results):
        pass

    def Reset(self):
        pass

    def EstimatePossibleOutcomes(self):
        last = 1
        total = 1


    # Простой алгоритм для вычисления комбинаций из N вещей, взятых R
    # за один раз.Единственное место, где это используется, - оценить,
    # сколько возможных исходов мы имеем дело с ситуациями,
    # включающими исчерпывающее перечисление.
    def CalculateCombinations(self, N, R):
        answer = 1
        multiplier = N
        divisor = 1
        k = min(N, N - R)

        while divisor <= k:
            answer = (answer * multiplier) / divisor
            multiplier-=1
            divisor+=1

        return answer