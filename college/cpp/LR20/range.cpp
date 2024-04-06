#include "range.h"

Range::Range(int start, int end) {
    this->start = start;
    this->end = end;
}

int Range::getStart() const
{
    return start;
}

int Range::getEnd() const
{
    return end;
}

bool Range::IsInRange(int n) const
{
    return n >= start && n <= end;
}
