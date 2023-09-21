#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {

    // declare variables
    double m, k, x, v, t_max, dt, t, a, x_prev;
    vector<double> t_list, x_list, v_list;

    // mass, spring constant, initial position and velocity
    m = 1;
    k = 1;
    x = 0;
    v = 1;

    // simulation time and timestep
    t_max = 100;
    dt = 0.1;
    t = 0;
    x_prev = -(v * dt - x);

    // Verlet integration
    for (int i = 0; i <= t_max / dt; i++, t += dt) {

        // append current state to trajectories
        t_list.push_back(t);
        x_list.push_back(x);
        v_list.push_back(v);


        // calculate new position and velocity
        a = -k * x / m;

        double x_current = x;

        x = 2 * x - x_prev + dt * dt * a;
        v = (x - x_current) / dt;

        x_prev = x_current;
    }

    // Write the trajectories to file
    ofstream fout;
    fout.open("verlet.txt");
    if (fout) { // file opened successfully
        for (int i = 0; i < t_list.size(); i = i + 1) {
            fout << t_list[i] << ' ' << x_list[i] << ' ' << v_list[i] << endl;
        }
    } else { // file did not open successfully
        cout << "Could not open trajectory file for writing" << endl;
    }

}