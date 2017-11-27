using System;

public static class Game
{
  public static float Combat(float health, float damage)
  // Given a starting float for health and a float for damage, return a float with the player's updated health.
  {
    Console.WriteLine("{0}, {1}", health, damage);
    float newHealth = health - damage;
    if (newHealth < 0){newHealth = 0;}
    return newHealth;
  }
}
