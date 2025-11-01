class BiddingAgent1:
    def __init__(self):
        pass

    def get_bid(self, num_of_agents, P, q, v):
        return v / 2.5

    def notify_outcome(self, reward, outcome, position):
        pass

    def get_id(self):
        return "id_n_l"





class BiddingAgent2:
    def __init__(self,
                 warmup_rounds: int = 1000,
                 base_margin: float = 0.03,
                 max_margin: float = 0.15,
                 ema_alpha: float = 0.025):
        # Parameters of agent 2
        self.exploration_rounds = warmup_rounds
        self.base_margin = base_margin
        self.max_margin = max_margin
        self.ema_alpha = ema_alpha
        self.round = 0
        self.avg_competitor_score = None
        self.margin = base_margin

    def get_bid(self, num_of_agents, P, q, v):
        self.round += 1
        # Stage 1 : For some number of "exploration_rounds"
        # we bid like we assume all other students will bid
        # (v/2.5 - as shown in lecture)
        if self.round <= self.exploration_rounds or self.avg_competitor_score is None:
            return v / 2.5

        # Stage 2 : Exploiting the data from stage 1
        # and bidding a bit higher than the runner-up while
        # NEVER bidding more than v
        target_score = self.avg_competitor_score * (1.0 + self.margin)
        bid = target_score / max(q, 1e-6)
        return min(bid, v)

    def notify_outcome(self, reward, payment, position):
        # In the case we won a spot in the auction,
        # runner-up's bid, is what we paid
        if position >= 0:
            if self.avg_competitor_score is None:
                self.avg_competitor_score = payment
            else:
                self.avg_competitor_score = ((1 - self.ema_alpha) * self.avg_competitor_score
                                                + self.ema_alpha * payment)
            self.margin = self.base_margin
        # In case we LOST in the auction
        else:
            self.margin = min(self.margin * 1.5, self.max_margin)

    def get_id(self):
        return "id_n_l"
