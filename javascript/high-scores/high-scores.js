export class HighScores {
  constructor(scoreList) {
    this.scoreList = scoreList
  }

  get scores() {
    return this.scoreList
  }

  get latest() {
    let scores=this.scoreList
    return scores[scores.length-1]
  }

  get personalBest() {
    let scores=this.scoreList
    return Math.max(...scores)
  }

  get personalTopThree() {
    let scores=this.scoreList
    let sortedScores=[...scores].sort((a, b) => b - a);
    return sortedScores.slice(0, 3);
  }
}
