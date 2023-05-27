## Pure pursuit implementation: for VEX

Basic features:
 * Circle intersection point finding
   * Idea: changing the size of the circle as required based on error or location from actual path
 * Navigation to point at instant
   * Bang bang navigation with set turn velocities
   * PID navigation with configuration - want the movement speed to be slower when the turning is greater - need a balancing algorithm for that
 * Need an algorithm to determine the segment and point of intersection in front