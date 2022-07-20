#include <bits/stdc++.h>

using namespace std;

#define tim 299

int no_of_cities;

string type;
vector<pair<double, double>> cities;
vector<vector<double>> adj;

mt19937 rnd(chrono::steady_clock::now().time_since_epoch().count());
uniform_int_distribution<int> dis(0, 499);

class chromo
{
public:
    int n;
    double value;
    vector<int> order;
    chromo()
    {
        ;
    }
    chromo(int N)
    {
        this->n = N;
        for (int i = 0; i < N; i++)
        {
            order.push_back(i);
        }
        shuffle(order.begin(), order.end(), rnd);
        this->value = cost();
    }
    pair<int, int> random_range()
    {
        int l, r;
        l = dis(rnd) % this->n;
        while (true)
        {
            r = dis(rnd) % this->n;
            if (r != l)
            {
                break;
            }
        }
        if (r < l)
        {
            swap(l, r);
        }
        return {l, r};
    }
    chromo mutate()
    {
        pair<int, int> range = random_range();
        chromo mutant = *this;
        reverse(mutant.order.begin() + range.first, mutant.order.begin() + range.second);
        mutant.value = mutant.cost();
        return mutant;
    } // may use another crossover function/technique; the one below is partially mapped crossover
    pair<chromo, chromo> crossover(chromo &partner)
    {
        chromo child1, child2;
        pair<int, int> range = random_range();
        for (int i = 0; i < n; i++)
        {
            bool check = false;
            for (int j = range.first; j <= range.second && !check; j++)
            {
                if (partner.order[j] == order[i])
                {
                    check = true;
                }
            }
            if (!check)
            {
                child1.order.push_back(order[i]);
            }
        }
        for (int i = range.first; i <= range.second; i++)
        {
            child1.order.push_back(partner.order[i]);
        }
        for (int i = 0; i < n; i++)
        {
            bool check = false;
            for (int j = range.first; j <= range.second && !check; j++)
            {
                if (order[j] == partner.order[i])
                {
                    check = true;
                }
            }
            if (!check)
            {
                child2.order.push_back(partner.order[i]);
            }
        }
        for (int i = range.first; i <= range.second; i++)
        {
            child2.order.push_back(order[i]);
        }
        child1.n = (int)child1.order.size();
        child2.n = (int)child2.order.size();
        child1.value = child1.cost();
        child2.value = child2.cost();
        return {child1, child2};
    }
    double cost()
    {
        double ans = 0.00;
        for (int i = 0; i < n; i++)
        {
            ans += adj[order[i]][order[(i + 1) % n]];
        }
        return ans;
    }
    void print()
    {
        cout << "Cost: " << value << endl;
        for (int i = 0; i < n; i++)
        {
            cout << order[i] << " ";
        }
        cout << endl;
    }
    bool operator<(chromo &a)
    {
        return this->value < a.value;
    }
};

class genalgo
{
    int mutation_count;
    int crossover_count;
    chromo ans;

public:
    genalgo(int m, int c)
    {
        mutation_count = m;
        crossover_count = c;
    }
    pair<int, int> randomInd(int m)
    {
        int l, r;
        l = dis(rnd) % m;
        while (true)
        {
            r = dis(rnd) % m;
            if (l != r)
            {
                break;
            }
        }
        if (r < l)
        {
            swap(l, r);
        }
        return {l, r};
    }
    void simulate()
    {
        auto start = chrono::high_resolution_clock::now();
        vector<chromo> popu;
        for (int i = 0; i < no_of_cities; i++)
        {
            popu.push_back(chromo(no_of_cities));
        }
        sort(popu.begin(), popu.end());
        ans = popu[0];
        ans.print();
        while (true)
        {
            for (int i = 0; i < crossover_count; i++)
            {
                pair<int, int> ind = randomInd((int)popu.size() / 2);
                pair<chromo, chromo> prod = popu[ind.first].crossover(popu[ind.second]);
                popu.push_back(prod.first);
                popu.push_back(prod.second);
            }
            for (int i = 0; i < mutation_count; i++)
            {
                int randomIndex = dis(rnd) % ((int)popu.size() / 2);
                chromo mutated = popu[randomIndex].mutate();
                popu.push_back(mutated);
            }
            for (int i = 0; i < (3 * no_of_cities); i++)
            {
                popu.push_back(chromo(no_of_cities));
            }
            sort(popu.begin(), popu.end());
            while ((int)popu.size() > no_of_cities)
            {
                popu.pop_back();
            }
            if (ans.value > popu[0].value)
            {
                ans = popu[0];
                ans.print();
            }
            auto end = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<chrono::seconds>(end - start).count();
            if (duration > tim)
            {
                break;
            }
        }
        ans.print();
    }
};

int main()
{
    cin >> type >> no_of_cities;
    double x, y;
    for (int i = 0; i < no_of_cities; i++)
    {
        cin >> x >> y;
        cities.push_back({x, y});
    }
    adj.resize(no_of_cities);
    for (int i = 0; i < no_of_cities; i++)
    {
        for (int j = 0; j < no_of_cities; j++)
        {
            cin >> x;
            adj[i].push_back(x);
        }
    }
    cout << fixed << setprecision(5);
    genalgo algo(50, 50);
    algo.simulate();
    return 0;
}