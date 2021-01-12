import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class Main {

// I got the following code from the solutions to hw2:
    public static void main(String[] args) {
        Scanner sc= null;
        if (args.length > 0) {
            try {
                sc= new Scanner(new File(args[0]));
            } catch (FileNotFoundException e1) {
                System.err.println("Can't find input file " + args[0]);
                return;
            }
        } else {
            sc= new Scanner(System.in);
        }
        new Main().go(sc);
    }

    Node[] nodes; //an array that stores all nodes
    Subset[] subsets; //an array that stores all union-find subsets

    private void go(Scanner sc) {
        int n= sc.nextInt(); // number of nodes (villages)
        int m= sc.nextInt(); // number of initial edges (roads)

        // create the nodes and the subsets
        nodes= new Node[n];
        subsets= new Subset[n];
        for (int i= 0; i < n; i++ ) {
            nodes[i]= new Node(i);
            // initially each node is a union-find subset
            subsets[i]= new Subset(i);
        }

        // add the edges and adjust the union-find subsets
        for (int i= 0; i < m; i++ ) {
            int i1= sc.nextInt();
            int i2= sc.nextInt();

            Node n1= nodes[i1];
            Node n2= nodes[i2];

            Node root1= find(n1); //the greatest parent of node1
            Node root2= find(n2); //the greatest parent of node2

            //if the two nodes are in different subsets, merge these subsets
            if (root1 != root2) {
                union(subsets[root1.name], subsets[root2.name]);
            }
        }

        //count the number of "existing" union-find subsets
        int subs= 0;
        for (int j= 0; j < n; j++ ) {
            if (subsets[j].root != -1) {
                subs++ ;
            }
        }

        //The number of roads that are needed is equal to the number of the existing subsets - 1
        System.out.println(Integer.toString(subs - 1));
    }

    //this function merges two subsets
    private void union(Subset s1, Subset s2) {
        Node root1= nodes[s1.root];
        Node root2= nodes[s2.root];
        //the greatest subsets continues existing
        if (s1.size > s2.size) {
            //the parent of the root of the smaller subsets becomes the root of the bigger subsets
            root2.parent= root1.name;
            //the smaller subset's root gets value -1 which means the subset doesn't exist anymore
            s2.root= -1;
            //the size of the bigger subset increases by the size of the smaller one
            s1.size= s1.size + s2.size;
        } else {
            root1.parent= root2.name;
            s1.root= -1;
            s2.size= s2.size + s1.size;
        }
    }

//this function finds the root of the subset of Node n
    private Node find(Node n) {
        int parent= n.parent;
        if (parent == n.name)
            return n;
        else
            return find(nodes[parent]);
    }

}

// Class representing a node
class Node {
    int name;
    int parent;

    Node(int n) {
        name= n;
        parent= n;
    }
}

// Class representing a union-find subset
class Subset {
    int root;
    int size;

    Subset(int n) {
        root= n;
        size= 1;
    }

}
