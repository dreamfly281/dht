/*
 * Copyright (c) 2003 [NAMES_GO_HERE]
 *                    Massachusetts Institute of Technology
 * 
 * Permission is hereby granted, free of charge, to any person obtaining
 * a copy of this software and associated documentation files (the
 * "Software"), to deal in the Software without restriction, including
 * without limitation the rights to use, copy, modify, merge, publish,
 * distribute, sublicense, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so, subject to
 * the following conditions:
 * 
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

#ifndef __TAPESTRY_OBSERVER_H
#define __TAPESTRY_OBSERVER_H

#include "p2psim/observer.h"
#include "protocols/tapestry.h"

class TapestryObserver : public Observer {
public:
  TapestryObserver(Args*);
  ~TapestryObserver();
  static TapestryObserver* Instance(Args*);
  virtual void kick(Observed *, ObserverInfo *);

private:
  static TapestryObserver *_instance;
  unsigned int _init_num;
  unsigned int _oracle_num;
  bool _stabilized;
  string _type;

  void init_state();

  vector<Tapestry::GUID> lid;
};

#endif // __TAPESTRY_OBSERVER_H
