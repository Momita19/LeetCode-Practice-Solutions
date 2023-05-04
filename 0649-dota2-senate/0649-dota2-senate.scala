import scala.collection.mutable.Queue

object Solution {
    def predictPartyVictory(senate: String): String = {
        val n = senate.length
        val dir = Queue[Int]()
        val rad = Queue[Int]()
        for((char,i) <- senate.zipWithIndex){
            if (char == 'R') rad.enqueue(i)
            else dir.enqueue(i)
        }
        while(rad.nonEmpty && dir.nonEmpty){
            val rIndex = rad.dequeue()
            val dIndex = dir.dequeue()
            
            if (rIndex < dIndex) rad.enqueue(rIndex+n)
            else dir.enqueue(dIndex+n)
        }
        if (rad.nonEmpty) "Radiant"
        else "Dire"
    
        
    }
}