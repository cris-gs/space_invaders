def bullet_hits_enemy(bullet, enemy) -> bool:
    return enemy.alive and bullet.x == enemy.x and bullet.y == enemy.y
