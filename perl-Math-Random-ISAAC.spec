%define upstream_name    Math-Random-ISAAC
%define upstream_version 1.004

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Pure Perl port of the ISAAC PRNG algorithm
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Math::Random::ISAAC::XS)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::NoWarnings)
BuildArch:	noarch

%description
As with other Pseudo-Random Number Generator (PRNG) algorithms like the
Mersenne Twister (see the Math::Random::MT manpage), this algorithm is
designed to take some seed information and produce seemingly random results
as output.

However, ISAAC (Indirection, Shift, Accumulate, Add, and Count) has
different goals than these commonly used algorithms. In particular, it's
really fast - on average, it requires only 18.75 machine cycles to generate
a 32-bit value. This makes it suitable for applications where a significant
amount of random data needs to be produced quickly, such solving using the
Monte Carlo method or for games.

The results are uniformly distributed, unbiased, and unpredictable unless
you know the seed. The algorithm was published by Bob Jenkins in the late
90s and despite the best efforts of many security researchers, no feasible
attacks have been found to date.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.4.0-3mdv2011.0
+ Revision: 657339
- rebuild for updated spec-helper

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 1.4.0-2
+ Revision: 640771
- rebuild to obsolete old packages

* Fri Feb 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.0-1
+ Revision: 638500
- update to new version 1.004

* Fri Jan 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-1
+ Revision: 633684
- import perl-Math-Random-ISAAC

