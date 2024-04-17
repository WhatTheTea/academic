#ifndef RANGE_H
#define RANGE_H

struct Range
{
public:
    Range(int start, int end);
    int getStart() const;
    int getEnd() const;
    bool IsInRange(int n) const;

private:
    int start = 0;
    int end = 0;
};

#endif // RANGE_H
